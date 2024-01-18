import inspect
import numpy as np

from .feature import Feature
from scipy import stats
from pm4py.statistics.traces.generic.log import case_statistics

class TraceVariant(Feature):
    def __init__(self, feature_names='trace_variant'):
        self.feature_type = "trace_variant"
        self.available_class_methods = dict(inspect.getmembers(TraceVariant, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def occurrences(log):
        variants_count = case_statistics.get_variant_statistics(log)
        variants_count = sorted(variants_count, key=lambda x: x["count"], reverse=True)
        result = [x["count"] for x in variants_count]

        return result

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


