import json
import pandas as pd

dataset_name = "v4.1"
feature_set_name = "medium"

from utils_old import (
    save_model,
    load_model,
    neutralize,
    validation_metrics,
    ERA_COL,
    DATA_TYPE_COL,
    TARGET_COL,
    EXAMPLE_PREDS_COL,
)


print("Loading data")

print("Open json file")
with open(f"{dataset_name}/features.json", "r") as f:
    feature_metadata = json.load(f)

# features = list(feature_metadata["feature_stats"].keys()) # get all the features
# features = feature_metadata["feature_sets"]["small"] # get the small feature set
features = feature_metadata["feature_sets"][
    feature_set_name
]  # get the medium feature set
target_cols = feature_metadata["targets"]
# read in just those features along with era and target columns
# read_columns = features + target_cols + [ERA_COL, DATA_TYPE_COL]

read_columns = [ERA_COL, DATA_TYPE_COL]

print(target_cols)
print(read_columns)

print("Set training data")
# note: sometimes when trying to read the downloaded data you get an error about invalid magic parquet bytes...
# if so, delete the file and rerun the napi.download_dataset to fix the corrupted file
training_data = pd.read_parquet(
    f"{dataset_name}/train_int8.parquet", columns=read_columns
)

print("it worked !!")

