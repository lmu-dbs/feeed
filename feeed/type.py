from .simple_stats import SimpleStats as simple_stats
from .trace_length import TraceLength as trace_length

import inspect

def feature_type(feature_name):
    feature_types = [
            "simple_stats",
            "trace_length",
            "trace_variant",
            "activities",
            "start_activities",
            "end_activities",
            "entropies",
            "complexity",
            "time_based",
        ]

    for feature_type in feature_types:
        if feature_type == 'simple_stats' or feature_type == 'trace_length':
            available_features = [member[0] for member in inspect.getmembers(eval(feature_type), predicate=inspect.ismethod)]
        else:
            available_features = []
        available_features.append(str(feature_type))
        if feature_name in available_features:
            return feature_type
    raise ValueError(f"ERROR: Invalid value for feature_key argument: {feature_name}. See README.md for supported feature_names or  Use a sublist of the following:"
            "\n['simple_stats', 'trace_length', 'trace_variant', 'activities', 'start_activities', 'end_activities',",
            " 'entropies', 'complexity', 'time_based] or None")