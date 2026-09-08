import inspect
import numpy as np
import editdistance

from .feature import Feature
from scipy import stats
from pm4py.statistics.traces.generic.log import case_statistics
from .simple_stats import SimpleStats
from pm4py.algo.filtering.log.variants import variants_filter

class TraceVariant(Feature):
    def __init__(self, feature_names='trace_variant'):
        self.feature_type = "trace_variant"
        self.available_class_methods = dict(inspect.getmembers(TraceVariant, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def occurrences(log, reverse = True):
        variants_count = case_statistics.get_variant_statistics(log)
        variants_count = sorted(variants_count, key=lambda x: x["count"], reverse=reverse)
        result = [x["count"] for x in variants_count]
        return result

    def distinct_traces_occurrences_sorted(log):
        trace_occurrences = dict()
        for trace in log:
            trace_rep = str(trace)
            if trace_rep not in trace_occurrences.keys():
                trace_occurrences[trace_rep] = 1
            else:
                trace_occurrences[trace_rep] += 1
        return dict(sorted(trace_occurrences.items(), key=lambda item: item[1]))

    @classmethod
    def ratio_most_common_variant(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[:1]) / len(log)

    @classmethod
    def ratio_top_1_variants(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[: int(len(occurrences) * 0.01)]) / len(log)

    @classmethod
    def ratio_top_5_variants(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[: int(len(occurrences) * 0.05)]) / len(log)

    @classmethod
    def ratio_top_10_variants(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[: int(len(occurrences) * 0.1)]) / len(log)

    @classmethod
    def ratio_top_20_variants(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[: int(len(occurrences) * 0.2)]) / len(log)

    @classmethod
    def ratio_top_50_variants(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[: int(len(occurrences) * 0.5)]) / len(log)

    @classmethod
    def ratio_top_75_variants(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return sum(occurrences[: int(len(occurrences) * 0.75)]) / len(log)

    @classmethod
    def mean_variant_occurrence(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return np.mean(occurrences)

    @classmethod
    def std_variant_occurrence(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return np.std(occurrences)

    @classmethod
    def skewness_variant_occurrence(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return stats.skew(occurrences)

    @classmethod
    def kurtosis_variant_occurrence(cls, log):
        occurrences = TraceVariant.occurrences(log)
        return stats.kurtosis(occurrences)

    @classmethod
    def coverage_variants(cls, log, threshold_factor = 0.8):
        support_sorted_by_frequency = TraceVariant.distinct_traces_occurrences_sorted(log)
        sum_of_included_frequencies = 0
        number_of_included_trace_variants = 0
        threshold = threshold_factor * len(log)
        for trace in support_sorted_by_frequency.keys():
            if sum_of_included_frequencies >= threshold:
                break
            sum_of_included_frequencies += support_sorted_by_frequency[str(trace)]
            number_of_included_trace_variants += 1
        return number_of_included_trace_variants

    @classmethod
    def rel_coverage_variants(cls, log):
        return TraceVariant.coverage_variants(log) / SimpleStats.n_variants(log)

    @classmethod
    def heterogeneity_rate_variants(cls, log):
        number_of_trace_variants = SimpleStats.n_variants(log)
        number_of_traces = len(log)
        return np.log(number_of_trace_variants) / np.log(number_of_traces)

    @classmethod
    def similarity_rate_variants(cls, log):
        support = variants_filter.get_variants(log)
        sum_of_edit_distances = 0
        for trace1 in support:
            for trace2 in support:
                edit_distance = editdistance.eval(trace1, trace2)
                sum_of_edit_distances += (1 - (edit_distance / np.max([len(trace1), len(trace2)])))
        # now, the sum of edit distances also includes those between a trace and
        # itself. We remove those from the sum, as they are all exactly 1.
        sum_of_edit_distances -= len(support)
        return sum_of_edit_distances / (len(support) * (len(support) - 1))
