import pandas as pd   #import the pandas library

parquet_file = 'userdata1.parquet'
parquet_file_2 = 'live.parquet'

data = pd.read_parquet(parquet_file_2, engine='pyarrow')

print("We did it")

print(data.shape)