#Install packages with scoring function and numerapi
#!git clone https://github.com/numerai/numerai-tools.git
#!mv numerai-tools/numerai_tools/scoring.py /content/
#!pip install numerapi

from numerapi import NumerAPI
import pandas as pd

napi = NumerAPI()

napi.list_datasets()

#Download example predictions, meta model preds, and live targets
napi.download_dataset("v4.2/meta_model.parquet")
napi.download_dataset("v4.2/validation_benchmark_models.parquet", "validation_benchmark_models.parquet")
napi.download_dataset("v4.2/validation_int8.parquet")

df_mm = pd.read_parquet("v4.2/meta_model.parquet")

#Get eras that have data from meta model
mm_eras = df_mm["era"].unique()

bm_val = pd.read_parquet("validation_benchmark_models.parquet")

#Get bechmark predictions only for eras that have meta model data
bm_val_recent = bm_val.loc[bm_val["era"].isin(mm_eras)]

#Do the same for live targets
live_targets = pd.read_parquet("v4.2/validation_int8.parquet", columns=["era","target"])
live_targets_recent = live_targets.loc[live_targets["era"].isin(mm_eras)]

from scoring import correlation_contribution

#correlation_contribution(predictions: pd.DataFrame, meta_model: pd.Series, live_targets: pd.Series)
mmc = correlation_contribution(bm_val_recent, df_mm["numerai_meta_model"], live_targets_recent["target"])