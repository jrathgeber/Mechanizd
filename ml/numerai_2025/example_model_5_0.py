from numerapi import NumerAPI
import pandas as pd
import json
napi = NumerAPI()

# use one of the latest data versions
DATA_VERSION = "v5.0"

# Download data
napi.download_dataset(f"{DATA_VERSION}/train.parquet")
napi.download_dataset(f"{DATA_VERSION}/features.json")

# Load data
feature_metadata = json.load(open(f"{DATA_VERSION}/features.json"))
features = feature_metadata["feature_sets"]["medium"] # use "all" for better performance. Requires more RAM.
train = pd.read_parquet(f"{DATA_VERSION}/train.parquet", columns=["era"]+features+["target"])

# For better models, join train and validation data and train on all of it.
# This would cause diagnostics to be misleading though.
# napi.download_dataset(f"{DATA_VERSION}/validation.parquet")
# validation = pd.read_parquet(f"{DATA_VERSION}/validation.parquet", columns=["era"]+features+["target"])
# validation = validation[validation["data_type"] == "validation"] # drop rows which don't have targets yet
# train = pd.concat([train, validation])

# Downsample for speed
train = train[train["era"].isin(train["era"].unique()[::4])]  # skip this step for better performance

# Train model
import lightgbm as lgb
model = lgb.LGBMRegressor(
    n_estimators=2000,
    learning_rate=0.01,
    max_depth=5,
    num_leaves=2**5-1,
    colsample_bytree=0.1
)
# We've found the following "deep" parameters perform much better, but they require much more CPU and RAM
# model = lgb.LGBMRegressor(
#     n_estimators=30_000,
#     learning_rate=0.001,
#     max_depth=10,
#     num_leaves=2**10,
#     colsample_bytree=0.1
#     min_data_in_leaf=10000,
# )
model.fit(
    train[features],
    train["target"]
)

# Define predict function
def predict(
    live_features: pd.DataFrame,
    live_benchmark_models: pd.DataFrame
 ) -> pd.DataFrame:
    live_predictions = model.predict(live_features[features])
    submission = pd.Series(live_predictions, index=live_features.index)
    return submission.to_frame("prediction")

# Pickle predict function
import cloudpickle
p = cloudpickle.dumps(predict)
with open("example_model.pkl", "wb") as f:
    f.write(p)

# Download file if running in Google Colab
try:
    from google.colab import files
    files.download('example_model.pkl')
except:
    pass