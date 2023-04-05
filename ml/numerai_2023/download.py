# -*- coding: utf-8 -*-

from numerapi import NumerAPI

napi = NumerAPI()

napi.download_current_dataset("v4.1/train.parquet", "train.parquet")
napi.download_current_dataset("v4.1/validation.parquet", "validation.parquet")
napi.download_current_dataset("v4.1/live.parquet", "live.parquet")
napi.download_current_dataset("v4.1/live_example_preds.parquet", "live_example_preds.parquet")
napi.download_current_dataset("v4.1/validation_example_preds.parquet", "validation_example_preds.parquet")
napi.download_current_dataset("v4.1/features.json", "features.json")
napi.download_current_dataset("v4.1/meta_model.parquet", "meta_model.parquet")