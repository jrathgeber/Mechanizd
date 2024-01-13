import pandas as pd

# Sample data
data = {
    'Name': ['Yang Zhou', 'Jane', 'Mary', 'Jack'],
    'Age': [30, 34, 58, 66],
    'City': ['London', 'Tokyo', 'Chicago', 'Tokyo']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] >= 30]

# Group by city
grouped_df = filtered_df.groupby('City')

# Compute the average age per city
average_age = grouped_df['Age'].mean()

# Create a new DataFrame with the reset index
result = average_age.reset_index(name='Average_Age')

print(result)
#       City  Average_Age
# 0  Chicago         58.0
# 1   London         30.0
# 2    Tokyo         50.0