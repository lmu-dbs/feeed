import json
import numpy as np
from feeed.feature_extractor import extract_features

#  Testing Extract features as a dictionary
features = extract_features("test_logs/Sepsis.xes", feature_types=["simple_stats","trace_length","trace_variant","activities","start_activities","end_activities","eventropies","epa_based"])

def default_handler(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    elif isinstance(obj, np.integer):
        return int(obj)
    else:
        raise TypeError('Object of type %s is not JSON serializable' % type(obj))

# Write the dictionary to a JSON file
with open("output.json", "w") as json_file:
    json.dump(features, json_file, default=default_handler)
