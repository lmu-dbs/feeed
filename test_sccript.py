import json
import numpy as np
from feeed.feature_extractor import extract_features

# Extract features as a dictionary
features = extract_features("test_logs/BPI_Challenge_2013_closed_problems.xes")

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
