import inspect
import numpy as np

from .feature import Feature
from pm4py.algo.filtering.log.attributes import attributes_filter
from scipy import stats

class Activities(Feature):
    def __init__(self, feature_names='activities'):
        self.feature_type='activities'
        self.available_class_methods = dict(inspect.getmembers(Activities, predicate=inspect.ismethod))
        if self.feature_type in feature_names:
            self.feature_names = [*self.available_class_methods.keys()]
        else:
            self.feature_names = feature_names

    def activities(log):
        return attributes_filter.get_attribute_values(log, "concept:name")

    @classmethod
    def n_unique_activities(cls, log):
        activities = Activities.activities(log)
        return len(activities)

    @classmethod
    def activities_min(cls, log):
        activities = Activities.activities(log)
        return np.min(list(activities.values()))

    @classmethod
    def activities_max(cls, log):
        activities = Activities.activities(log)
        return np.max(list(activities.values()))

    @classmethod
    def activities_mean(cls, log):
        activities = Activities.activities(log)
        return np.mean(list(activities.values()))

    @classmethod
    def activities_median(cls, log):
        activities = Activities.activities(log)
        return np.median(list(activities.values()))

    @classmethod
    def activities_std(cls, log):
        activities = Activities.activities(log)
        return np.std(list(activities.values()))

    @classmethod
    def activities_variance(cls, log):
        activities = Activities.activities(log)
        return np.var(list(activities.values()))

    @classmethod
    def activities_q1(cls, log):
        activities = Activities.activities(log)
        return np.percentile(list(activities.values()), 25)

    @classmethod
    def activities_q3(cls, log):
        activities = Activities.activities(log)
        return np.percentile(list(activities.values()), 75)

    @classmethod
    def activities_iqr(cls, log):
        activities = Activities.activities(log)
        return stats.iqr(list(activities.values()))

    @classmethod
    def activities_skewness(cls, log):
        activities = Activities.activities(log)
        return stats.skew(list(activities.values()))

    @classmethod
    def activities_kurtosis(cls, log):
        activities = Activities.activities(log)
        return stats.kurtosis(list(activities.values()))

