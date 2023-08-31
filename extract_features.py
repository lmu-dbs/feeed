import os
import pandas as pd
from tqdm import tqdm
from feeed import extract_features, sort_files, feature_names


path = "test_logs"
combined_features = pd.DataFrame()

print("Extracting features")

for file in tqdm(sort_files(os.listdir(path))):
    features = extract_features(path+"/"+file)
    temp = pd.DataFrame.from_dict([features])
    combined_features = pd.concat([combined_features, temp], ignore_index=True)

combined_features.to_csv("log_features.csv", index=False)
