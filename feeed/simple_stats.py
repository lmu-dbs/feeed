from pm4py.algo.filtering.log.variants import variants_filter

import inspect

class SimpleStats:
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


def simple_stats(log):
    available_class_methods = inspect.getmembers(SimpleStats, predicate=inspect.ismethod)
    output = {}
    for feature_name, feature_fn in available_class_methods:
        feature_value = feature_fn(log)
        output[f"{feature_name}"] = feature_value

    return output
