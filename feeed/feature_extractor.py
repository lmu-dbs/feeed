from .simple_stats import SimpleStats as simple_stats
from .trace_length import TraceLength as trace_length
from .trace_variant import trace_variant
from .activities import activities
from .start_activities import start_activities
from .end_activities import end_activities
from .entropies import entropies
from .complexity import complexity
from .time import time_based

from datetime import datetime as dt
from pm4py.objects.log.importer.xes import importer as xes_importer

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
            available_features = [*eval(feature_type)().available_class_methods]
        else:
            available_features = []
        available_features.append(str(feature_type))
        if feature_name in available_features:
            return feature_type
    raise ValueError(f"ERROR: Invalid value for feature_key argument: {feature_name}. See README.md for supported feature_names or  Use a sublist of the following:"
            "\n['simple_stats', 'trace_length', 'trace_variant', 'activities', 'start_activities', 'end_activities',",
            " 'entropies', 'complexity', 'time_based] or None")

def extract_features(event_logs_path, feature_types=None):
    log_name = event_logs_path.rsplit("/", 1)[-1]
    log = xes_importer.apply(
        f"{event_logs_path}", parameters={"show_progress_bar": False}
    )

    if feature_types is None:
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

    features = {"log": log_name.split(".xes")[0]}
    start_log = dt.now()

    for i, ft_name in enumerate(feature_types):
        start_feat = dt.now()
        ft_type = feature_type(ft_name)

        if ft_type == "entropies" or ft_type == "complexity":
            feature_values = eval(f"{ft_type}(event_logs_path)")#Add feature_names parameter here and default in fnc
        else:
            feature_values = eval(f"{ft_type}(feature_names=['{ft_name}']).extract(log)")
        features = {**features, **feature_values}

        log_info =  f"     INFO: {log_name} starting at {len(features)}, {ft_name} from {ft_type} took {dt.now()-start_feat} sec, "
        if i == len(feature_types) - 1:
            print(log_info + "last feature.")
        else:
            print(log_info + f"next {feature_types[(i+1)%len(feature_types)]}...")
    print(
        f"SUCCESSFULLY: {len(features)} features for {log_name} took {dt.now() - start_log} sec."
    )
    return features
