
import pandas as pd

dataset_name = "v4.1"

training_data = pd.read_parquet(
    f"{dataset_name}/train_int8.parquet"
)

print("it worked")

training_data.shape