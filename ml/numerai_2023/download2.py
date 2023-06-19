from numerapi import NumerAPI
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

# Numerai credentials for submission
public = config['numerai']['public']
secret = config['numerai']['secret']


contest = str(501)
directory = 'F:\\Numerai\\numerai' + contest + '\\'

napi = NumerAPI(public, secret)
#napi.download_dataset(directory + "v4.1/train.parquet", "train.parquet")
napi.download_dataset(directory + "v4.1/validation.parquet", "validation.parquet")
napi.download_dataset(directory + "v4.1/live.parquet", "live.parquet")
napi.download_dataset(directory + "v4.1/live_example_preds.parquet", "live_example_preds.parquet")
napi.download_dataset(directory + "v4.1/validation_example_preds.parquet", "validation_example_preds.parquet")
napi.download_dataset(directory + "v4.1/features.json", "features.json")
napi.download_dataset(directory + "v4.1/meta_model.parquet", "meta_model.parquet")