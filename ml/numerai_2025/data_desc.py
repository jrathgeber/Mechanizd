import pandas

def printList1(list, col, STR_FMT='{}', gap=1):
    list = [STR_FMT.format(x).lstrip() for x in list]
    FMT2 = '%%%ds%%s' % (max(len(x) for x in list)+gap)
    print(''.join([FMT2 % (v, "" if (i+1) % col else "\n") for i, v in enumerate(list)]))


contest = str(505)
directory = 'F:/Numerai/numerai' + contest + '/'
dataset_name = "v4.3"

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

printList1( column_names, 5 )

eras = df.era
print ("") # There are 120 eras numbered from 1 to 120
print ("eras.describe()")
print (eras.describe())

print ("") # The earlier eras are smaller, but generally each era is 4000-5000 rows
print ("df.groupby(eras).size().plot()")
df.groupby(eras).size().plot()
