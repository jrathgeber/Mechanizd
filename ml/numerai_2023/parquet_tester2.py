import pandas as pd   #import the pandas library

parquet_file = 'userdata1.parquet'
parquet_file_2 = 'live.parquet'
parquet_file_3 = 'live_int8_509.parquet'

data = pd.read_parquet(parquet_file_3, engine='pyarrow')

print("We did it")

print(data.shape)