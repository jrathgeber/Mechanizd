import pandas

contest = str(503)
directory = 'F:/Numerai/numerai' + contest + '/'
dataset_name = "v4.1"

print(contest)

df = pandas.read_parquet(
    f"{directory + dataset_name}/train_int8.parquet"
)

print("df.shape")
print(df.shape)