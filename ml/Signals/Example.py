import configparser

from numerapi import NumerAPI, SignalsAPI
import pandas as pd

napi = NumerAPI()

# Use int8 to save on storage and memory
# napi.download_dataset("signals/v1.0/train.parquet")
training_data = pd.read_parquet("signals/v1.0/train.parquet")

import lightgbm as lgb

features = [
      f for f in training_data.columns
      # there are two non-numerical feature cols
      if "feature" in f and f not in ("feature_country", "feature_exchange_code")
]

model = lgb.LGBMRegressor(
      n_estimators=200,
      learning_rate=0.01,
      max_depth=5,
      num_leaves=2 ** 5,
      colsample_bytree=0.1
)
model.fit(
      training_data[features],
      training_data["target"]
)


config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

# Numerai credentials for submission
public = config['numerai']['public']
secret = config['numerai']['secret']

sapi = SignalsAPI(public, secret)

# Download latest live features
sapi.download_dataset(f"signals/v1.0/live.parquet")
live_data = pd.read_parquet(f"signals/v1.0/live.parquet")

#features = [f for f in live_data.columns if "feature" in f]

features_l = [
      f for f in live_data.columns
      # there are two non-numerical feature cols
      if "feature" in f and f not in ("feature_country", "feature_exchange_code")
]

live_features = live_data[features]

# Generate live predictions
live_predictions = model.predict(live_data[features])

# Format and save submission
submission = pd.Series(
    live_predictions, index=live_features.index
).to_frame("prediction")
submission.to_csv(f"submission.csv")

# Upload submission
sapi.upload_predictions(f"submission.csv")