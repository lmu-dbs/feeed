import warnings
import numpy as np
import pandas as pd
from scipy import stats


"""
Implementing each time-based feature as `@classmethods` within this class allows us to scale and manage features easily. 
A current bottleneck is that each class method should accept `**kwargs` regardless of the other arguments, which
can be internally handled in the future. Each class method is accessed by inspecting the object using `inspect.getmembers`.

All the time features are currently measured in seconds, and they include:

- `execution_time`: execution time of an event w.r.t. to the previous one
- `accumulated_time`: accumulated time of an event w.r.t. to the first one from a trace
- `remaining_time`: remaining time of an event w.r.t. to the last one from a trace
- `within_day`: time within the day 

Essentially, there are methods that accept `group` or `X` as arguments. The former consists of a trace (i.e., grouped by case id) since we evaluate, for instance, the event timestamp with the previous one. The latter consists of the whole event log, since some operations can be performed element-wise (e.g., extracting the weekday from a timestamp column).
"""

warnings.filterwarnings("ignore")

# try:
#     import os
#     import pandarallel
#     has_pandarallel = True
# except:
#     has_pandarallel = False

class Timestamp:
    """
    ref: https://github.com/raseidi/skpm/blob/main/skpm/event_feature_extraction/_time.py#L124
    """
    @classmethod
    def execution_time(cls, group, ix_list, time_col="time:timestamp", **kwargs):
        return group[time_col].diff().loc[ix_list].dt.total_seconds().fillna(0)

    @classmethod
    def accumulated_time(cls, group, ix_list, time_col="time:timestamp", **kwargs):
        return (
            group[time_col].apply(lambda x: x - x.min()).loc[ix_list].dt.total_seconds()
        )  

    @classmethod
    def remaining_time(cls, group, ix_list, time_col="time:timestamp", **kwargs):
        return (
            group[time_col].apply(lambda x: x.max() - x).loc[ix_list].dt.total_seconds()
        )  

    @classmethod
    def within_day(cls, X, time_col="time:timestamp", **kwargs):
        # pd = check_pandas_support(
        #     "'pandas' not found. Please install it to use this method."
        # )
        return (
            pd.to_timedelta(X[time_col].dt.time.astype(str)).dt.total_seconds().values
        )

def get_available_time_features():
    import inspect
    class_methods = inspect.getmembers(Timestamp, predicate=inspect.ismethod)
    return class_methods

def meta(time):
    time_min = np.min(time)
    time_max = np.max(time)
    time_mean = np.mean(time)
    time_median = np.median(time)
    time_mode = stats.mode(time, keepdims=True)[0][0]
    time_std = np.std(time)
    time_variance = np.var(time)
    time_q1 = np.percentile(time, 25)
    time_q3 = np.percentile(time, 75)
    time_iqr = stats.iqr(time)
    time_geometric_mean = stats.gmean(time+1)
    time_geometric_std = stats.gstd(time+1)
    time_harmonic_mean = stats.hmean(time)
    time_skewness = stats.skew(time)
    time_kurtosis = stats.kurtosis(time)
    time_coefficient_variation = stats.variation(time)
    time_entropy = stats.entropy(time)
    time_hist, _ = np.histogram(time, density=True)
    time_skewness_hist = stats.skew(time_hist)
    time_kurtosis_hist = stats.kurtosis(time_hist)

    return {
        "time_min": time_min,
        "time_max": time_max,
        "time_mean": time_mean,
        "time_median": time_median,
        "time_mode": time_mode,
        "time_std": time_std,
        "time_variance": time_variance,
        "time_q1": time_q1,
        "time_q3": time_q3,
        "time_iqr": time_iqr,
        "time_geometric_mean": time_geometric_mean,
        "time_geometric_std": time_geometric_std,
        "time_harmonic_mean": time_harmonic_mean,
        "time_skewness": time_skewness,
        "time_kurtosis": time_kurtosis,
        "time_coefficient_variation": time_coefficient_variation,
        "time_entropy": time_entropy,
        # **{f"time_hist{i}": t for i, t in enumerate(time_hist)},
        "time_skewness_hist": time_skewness_hist,
        "time_kurtosis_hist": time_kurtosis_hist,
    }

def time_based(log):
    # if has_pandarallel:
    #     # parallelizes pandas apply
    #     pandarallel.initialize(nb_workers=min(os.cpu_count(), 20))
    
    if not isinstance(log, pd.DataFrame):
        import pm4py
        l = pm4py.convert_to_dataframe(log)
    else:
        l = log.copy()
    
    try:
        l["time:timestamp"] = pd.to_datetime(l["time:timestamp"])
    except:
        l["time:timestamp"] = pd.to_datetime(l["time:timestamp"], format="mixed")
    l = l.sort_values(by=["time:timestamp"]).reset_index(drop=True)
    available_features = get_available_time_features()
    group = l.groupby("case:concept:name", as_index=False, observed=True, group_keys=False)
    kwargs = {
        "group": group,
        "ix_list": l.index,
        "time_col": "time:timestamp",
        "X": l,
    }

    # time features extraction
    for feature_name, feature_fn in available_features:
        l[feature_name] = feature_fn(**kwargs)
    
    # meta features (stats) extraction 
    available_features = [f[0] for f in available_features]
    time_features = l[available_features].apply(lambda x: meta(x))
    time_features = time_features.to_dict()
    # flattening the output dict to follow the original demo format
    results = dict()
    for tf in time_features:
        results.update({f"{tf}_{k}": v for k,v in time_features[tf].items()})
    
    return results
