import inspect
import numpy as np
from scipy import stats

class TraceLength:
    def trace_lengths(log):
        trace_lengths = []
        n_events = 0
        for trace in log:
            n_events += len(trace)
            trace_lengths.append(len(trace))
        return trace_lengths

    def trace_len_hist(log):
        trace_lengths = TraceLength.trace_lengths(log)
        result,  _ = np.histogram(trace_lengths, density=True)
        return result

    @classmethod
    def trace_len_min(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.min(trace_lengths)

    @classmethod
    def trace_len_max(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.max(trace_lengths)

    @classmethod
    def trace_len_mean(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.mean(trace_lengths)

    @classmethod
    def trace_len_median(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.median(trace_lengths)

    @classmethod
    def trace_len_mode(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.mode(trace_lengths, keepdims=False)[0]

    @classmethod
    def trace_len_std(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.std(trace_lengths)

    @classmethod
    def trace_len_variance(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.var(trace_lengths)

    @classmethod
    def trace_len_q1(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.percentile(trace_lengths, 25)

    @classmethod
    def trace_len_q3(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return np.percentile(trace_lengths, 75)

    @classmethod
    def trace_len_iqr(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.iqr(trace_lengths)

    @classmethod
    def trace_len_geometric_mean(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.gmean(trace_lengths)

    @classmethod
    def trace_len_geometric_std(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        try:
            result=stats.gstd(trace_lengths)
        except:
            result=stats.gstd([i for idx, i in enumerate(trace_lengths) if trace_lengths[idx] != 0])
        return result

    @classmethod
    def trace_len_harmonic_mean(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.hmean(trace_lengths)

    @classmethod
    def trace_len_skewness(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.skew(trace_lengths)

    @classmethod
    def trace_len_kurtosis(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.kurtosis(trace_lengths)

    @classmethod
    def trace_len_coefficient_variation(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.variation(trace_lengths)

    @classmethod
    def trace_len_entropy(cls, log):
        trace_lengths = TraceLength.trace_lengths(log)
        return stats.entropy(trace_lengths)


    @classmethod
    def trace_len_skewness_hist(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return stats.skew(trace_len_hist)

    @classmethod
    def trace_len_kurtosis_hist(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return stats.kurtosis(trace_len_hist)

def trace_length(log, feature_names=None):
    if feature_names is None:
        feature_names = [
                'trace_len_min',
                'trace_len_max',
                'trace_len_mean',
                'trace_len_median',
                'trace_len_mode',
                'trace_len_std',
                'trace_len_variance',
                'trace_len_q1',
                'trace_len_q3',
                'trace_len_iqr',
                'trace_len_geometric_mean',
                'trace_len_geometric_std',
                'trace_len_harmonic_mean',
                'trace_len_skewness',
                'trace_len_kurtosis',
                'trace_len_coefficient_variation',
                'trace_len_entropy',
                'trace_len_hist1',
                'trace_len_hist2',
                'trace_len_hist3',
                'trace_len_hist4',
                'trace_len_hist5',
                'trace_len_hist6',
                'trace_len_hist7',
                'trace_len_hist8',
                'trace_len_hist9',
                'trace_len_hist10',
                'trace_len_skewness_hist',
                'trace_len_kurtosis_hist'
                ]
    available_class_methods = dict(inspect.getmembers(TraceLength, predicate=inspect.ismethod))

    output = {}
    for feature_name in feature_names:
        feature_fn = available_class_methods[feature_name]
        feature_value = feature_fn(log)
        output[f"{feature_name}"] = feature_value

    return output
