from numerapi import NumerAPI
import configparser

# Get Reference to Properties
config = configparser.ConfigParser()
config.read('C:\etc\properties.ini')

# Numerai credentials for submission
public = config['numerai']['public']
secret = config['numerai']['secret']

contest = str(504)

directory = 'F:\\Numerai\\numerai' + contest + '\\'

napi = NumerAPI(public, secret)

current_round = napi.get_current_round()

dataset_name = "v4.3"

from numerapi import NumerAPI

napi = NumerAPI()

# Let's see what files are available for download in the latest v4.2 dataset
var = [f for f in napi.list_datasets() if f.startswith("v4.3")]

print(var)

# Download the training data
napi.download_dataset( f"{dataset_name}/features.json", f"{directory + dataset_name}/features.json",)
napi.download_dataset( f"{dataset_name}/live_int8.parquet", f"{directory + dataset_name}/live_int8.parquet",)
napi.download_dataset( f"{dataset_name}/live_example_preds.csv", f"{directory + dataset_name}/live_example_preds.csv",)
napi.download_dataset( f"{dataset_name}/live_example_preds.parquet", f"{directory + dataset_name}/live_example_preds.parquet",)
napi.download_dataset( f"{dataset_name}/meta_model.parquet", f"{directory + dataset_name}/meta_model.parquet",)
napi.download_dataset( f"{dataset_name}/train_int8.parquet", f"{directory + dataset_name}/train_int8.parquet",)
napi.download_dataset( f"{dataset_name}/validation_example_preds.parquet", f"{directory + dataset_name}/validation_example_preds.parquet",)
napi.download_dataset( f"{dataset_name}/validation_int8.parquet", f"{directory + dataset_name}/validation_int8.parquet",)

napi.download_dataset(f"{dataset_name}/live_benchmark_models.parquet", f"{directory + dataset_name}/live_benchmark_models.parquet")
napi.download_dataset(f"{dataset_name}/validation_benchmark_models.parquet", f"{directory + dataset_name}/validation_benchmark_models.parquet")
napi.download_dataset(f"{dataset_name}/train_benchmark_models.parquet", f"{directory + dataset_name}/train_benchmark_models.parquet")

#
#napi.download_dataset("v4.3/features.json", "features.json")
#napi.download_dataset("v4.3/live_int8.parquet", "live_int8.parquet")
#napi.download_dataset("v4.3/live_example_preds.parquet", "live_example_preds.parquet")
#napi.download_dataset("v4.3/meta_model.parquet", "meta_model.parquet")
#napi.download_dataset("v4.3/train_int8.parquet", "train_int8.parquet")
#napi.download_dataset("v4.3/validation_example_preds.parquet", "validation_example_preds.parquet")
#napi.download_dataset("v4.3/validation_int8.parquet", "validation_int8.parquet")

#napi.download_dataset("v4.3/live_benchmark_models.parquet", "live_benchmark_models.parquet")
#napi.download_dataset("v4.3/validation_benchmark_models.parquet", "validation_benchmark_models.parquet")

