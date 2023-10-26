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
# print(df.describe())

# Get the list of all column names from headers
column_names = list(df.columns.values)
print("df.shape")
print(column_names)


eras = df.era
print ("") # There are 120 eras numbered from 1 to 120
print ("eras.describe()")
print (eras.describe())

print ("") # The earlier eras are smaller, but generally each era is 4000-5000 rows
print ("df.groupby(eras).size().plot()")
df.groupby(eras).size().plot()
