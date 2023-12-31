import numpy as np
from scipy import stats


def trace_length(log):
    trace_lengths = []
    n_events = 0
    for trace in log:
        n_events += len(trace)
        trace_lengths.append(len(trace))

    trace_len_min = np.min(trace_lengths)
    trace_len_max = np.max(trace_lengths)
    trace_len_mean = np.mean(trace_lengths)
    trace_len_median = np.median(trace_lengths)
    trace_len_mode = stats.mode(trace_lengths, keepdims=False)[0]
    trace_len_std = np.std(trace_lengths)
    trace_len_variance = np.var(trace_lengths)
    trace_len_q1 = np.percentile(trace_lengths, 25)
    trace_len_q3 = np.percentile(trace_lengths, 75)
    trace_len_iqr = stats.iqr(trace_lengths)
    trace_len_geometric_mean = stats.gmean(trace_lengths)
    trace_len_geometric_std = stats.gstd(trace_lengths)
    trace_len_harmonic_mean = stats.hmean(trace_lengths)
    trace_len_skewness = stats.skew(trace_lengths)
    trace_len_kurtosis = stats.kurtosis(trace_lengths)
    trace_len_coefficient_variation = stats.variation(trace_lengths)
    trace_len_entropy = stats.entropy(trace_lengths)
    trace_len_hist, _ = np.histogram(trace_lengths, density=True)
    trace_len_skewness_hist = stats.skew(trace_len_hist)
    trace_len_kurtosis_hist = stats.kurtosis(trace_len_hist)

    results = {
            "trace_len_min": trace_len_min,
            "trace_len_max": trace_len_max,
            "trace_len_mean": trace_len_mean,
            "trace_len_median": trace_len_median,
            "trace_len_mode": trace_len_mode,
            "trace_len_std": trace_len_std,
            "trace_len_variance": trace_len_variance,
            "trace_len_q1": trace_len_q1,
            "trace_len_q3": trace_len_q3,
            "trace_len_iqr": trace_len_iqr,
            "trace_len_geometric_mean": trace_len_geometric_mean,
            "trace_len_geometric_std": trace_len_geometric_std,
            "trace_len_harmonic_mean": trace_len_harmonic_mean,
            "trace_len_skewness": trace_len_skewness,
            "trace_len_kurtosis": trace_len_kurtosis,
            "trace_len_coefficient_variation": trace_len_coefficient_variation,
            "trace_len_entropy": trace_len_entropy,
            "trace_len_hist1": trace_len_hist[0],
            "trace_len_hist2": trace_len_hist[1],
            "trace_len_hist3": trace_len_hist[2],
            "trace_len_hist4": trace_len_hist[3],
            "trace_len_hist5": trace_len_hist[4],
            "trace_len_hist6": trace_len_hist[5],
            "trace_len_hist7": trace_len_hist[6],
            "trace_len_hist8": trace_len_hist[7],
            "trace_len_hist9": trace_len_hist[8],
            "trace_len_hist10": trace_len_hist[9],
            "trace_len_skewness_hist": trace_len_skewness,
            "trace_len_kurtosis_hist": trace_len_kurtosis
            }
    return results
