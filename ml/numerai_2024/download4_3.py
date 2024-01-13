from numerapi import NumerAPI
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

# Numerai credentials for submission
public = config['numerai']['public']
secret = config['numerai']['secret']

contest = str(503)

directory = 'F:\\Numerai\\numerai' + contest + '\\'

napi = NumerAPI(public, secret)

current_round = napi.get_current_round()

dataset_name = "v4.2"

from numerapi import NumerAPI

napi = NumerAPI()

# Let's see what files are available for download in the latest v4.2 dataset
[f for f in napi.list_datasets() if f.startswith("v4.2")]

# Download the training data
napi.download_dataset( f"{dataset_name}/features.json", f"{directory + dataset_name}/features.json",)
napi.download_dataset( f"{dataset_name}/live_int8.parquet", f"{directory + dataset_name}/live_int8.parquet",)
napi.download_dataset( f"{dataset_name}/live_example_preds.csv", f"{directory + dataset_name}/live_example_preds.csv",)
napi.download_dataset( f"{dataset_name}/live_example_preds.parquet", f"{directory + dataset_name}/live_example_preds.parquet",)
napi.download_dataset( f"{dataset_name}/meta_model.parquet", f"{directory + dataset_name}/meta_model.parquet",)
napi.download_dataset( f"{dataset_name}/train_int8.parquet", f"{directory + dataset_name}/train_int8.parquet",)
napi.download_dataset( f"{dataset_name}/validation_example_preds.parquet", f"{directory + dataset_name}/validation_example_preds.parquet",)
napi.download_dataset( f"{dataset_name}/validation_int8.parquet", f"{directory + dataset_name}/validation_int8.parquet",)




