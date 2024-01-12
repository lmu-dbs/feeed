import inspect

from pm4py.algo.filtering.log.variants import variants_filter
from .feature import Feature


class SimpleStats(Feature):
    def __init__(self, feature_names='simple_stats'):
        self.feature_type = "simple_stats"
        self.available_class_methods = dict(inspect.getmembers(SimpleStats, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [
                    "n_traces",
                    "n_unique_traces",
                    "ratio_unique_traces_per_trace"
                    ]
        else:
            self.feature_names = feature_names


    @classmethod
    def n_traces(cls, log):
        return len(log)

    @classmethod
    def n_unique_traces(cls, log):
        variants = variants_filter.get_variants(log)
        return len(variants)

    @classmethod
    def ratio_unique_traces_per_trace(cls, log):
        variants = variants_filter.get_variants(log)
        return len(variants)/len(log)
