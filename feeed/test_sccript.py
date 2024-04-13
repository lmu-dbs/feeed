import json
import numpy as np
from feeed.feature_extractor import extract_features

# Extract features as a dictionary
features = extract_features("test_logs/Sepsis.xes")

# Convert np.int32 values to int
def convert(obj):
    if isinstance(obj, np.int32):
        return int(obj)
    else:
        return obj

# Write the dictionary to a JSON file
with open("output.json", "w") as json_file:
    json.dump(features, json_file, default=convert)
