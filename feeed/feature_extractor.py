from .simple_stats import simple_stats
from .trace_length import trace_length
from .trace_variant import trace_variant
from .activities import activities
from .start_activities import start_activities
from .end_activities import end_activities
from .entropies import entropies
from .complexity import complexity
from .time import time_based

from datetime import datetime as dt
from pm4py.objects.log.importer.xes import importer as xes_importer


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

    try:
        for i, ft_type in enumerate(feature_types):
            start_feat = dt.now()
            if ft_type == "entropies" or ft_type == "complexity":
                feature_values = eval(f"{ft_type}(event_logs_path)")
            else:
                feature_values = eval(f"{ft_type}(log)")
            features = {**features, **feature_values}

            log_info = f"     INFO: {log_name} {len(features)-1} {ft_type} took {dt.now()-start_feat} sec, "
            if i == len(feature_types) - 1:
                print(log_info + "last feature.")
            else:
                print(log_info + f"next {feature_types[(i+1)%len(feature_types)]}...")
        print(
            f"SUCCESSFULLY: {len(features)} features for {log_name} took {dt.now() - start_log} sec."
        )
    except (NameError, TypeError):
        print(f"Invalid value for feature_types argument. Use a sublist of the following:"
              "\n['simple_stats', 'trace_length', 'trace_variant', 'activities', 'start_activities', 'end_activities',",
              " 'entropies', 'complexity', 'time_based] or None")

    return features
