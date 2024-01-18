import inspect
import numpy as np

from .feature import Feature
from scipy import stats

class TraceLength(Feature):
    def __init__(self, feature_names='trace_length'):
        self.feature_type="trace_length"
        self.available_class_methods = dict(inspect.getmembers(TraceLength, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

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
    def trace_len_hist1(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[0]

    @classmethod
    def trace_len_hist2(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[1]

    @classmethod
    def trace_len_hist3(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[2]

    @classmethod
    def trace_len_hist4(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[3]

    @classmethod
    def trace_len_hist5(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[4]

    @classmethod
    def trace_len_hist6(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[5]

    @classmethod
    def trace_len_hist7(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[6]

    @classmethod
    def trace_len_hist8(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[7]

    @classmethod
    def trace_len_hist9(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[8]

    @classmethod
    def trace_len_hist10(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return trace_len_hist[9]

    @classmethod
    def trace_len_skewness_hist(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return stats.skew(trace_len_hist)

    @classmethod
    def trace_len_kurtosis_hist(cls, log):
        trace_len_hist = TraceLength.trace_len_hist(log)
        return stats.kurtosis(trace_len_hist)
