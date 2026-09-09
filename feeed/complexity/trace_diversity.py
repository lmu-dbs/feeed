import inspect
import numpy as np

from pm4py.algo.filtering.log.variants import variants_filter
from ..feature import Feature
from .comparison_based import ComparisonBased
from .distinct_activities import DistinctActivities
from ..trace_length import TraceLength
from ..activities import Activities

class TraceDiversity(Feature):
    def __init__(self, feature_names='trace_diversity'):
        self.feature_type = "trace_diversity"
        self.available_class_methods = dict(inspect.getmembers(TraceDiversity, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    @classmethod
    def simple_trace_diversity(cls, log):
        return 1 - (DistinctActivities.distinct_activities_mean(log) / Activities.n_unique_activities(log))

    @classmethod
    def advanced_trace_diversity(cls, log):
        support = variants_filter.get_variants(log)
        return ComparisonBased.average_edit_distance(support) / TraceLength.trace_len_mean(log)
