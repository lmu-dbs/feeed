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


def simple_stats(log, feature_names=None):
    if feature_names is None:
        feature_names = [
                "n_traces",
                "n_unique_traces",
                "ratio_unique_traces_per_trace"
                ]

    available_class_methods = dict(inspect.getmembers(SimpleStats, predicate=inspect.ismethod))
    output = {}
    for feature_name in feature_names:
        feature_fn = available_class_methods[feature_name]
        feature_value = feature_fn(log)
        output[f"{feature_name}"] = feature_value

    return output
