import pandas as pd

file = 'C:\\Users\\Jason\\OneDrive\\Desktop\\data.xlsx'

sheet1 = pd.read_excel(file,
                        sheet_name = 0,
                        index_col = 0)

sheet2 = pd.read_excel(file,
                        sheet_name = 1,
                        index_col = 0)

# concatinating both the sheets
newData = pd.concat([sheet1, sheet2])

#print(newData)
#print(newData.head())
#print(newData.tail())

print(newData.shape)
sorted_column = newData.sort_values(['English'], ascending=True)
print(sorted_column.head(5))

#mat = newData['Math'].head()
#print(mat)

print(newData.describe())

newData['Total Marks'] = newData["English"] + newData["Math"] + newData["Science"]

print(newData['Total Marks'].head())

newData.to_excel('Output File.xlsx')