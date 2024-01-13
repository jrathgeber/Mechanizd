import pandas as pd

print("-")

# Sample data
data = {
    'Name': ['Yang Zhou', 'Jane', 'Mary', 'Jack'],
    'Age': [30, 34, 58, 66],
    'City': ['London', 'Tokyo', 'Chicago', 'Tokyo']
}

print(data)

# Create a DataFrame
df = pd.DataFrame(data)

print("-")
print(df)

# Use chained methods to clean data and compute statistics
result = (df
          .query('Age >= 30')  # Filter rows where Age is greater than 30
          .groupby('City')  # Group by city
          .agg(Average_Age=('Age', 'mean'))  # Compute the average age per city
          .reset_index()  # Reset index to turn 'City' back into a column
          )

print("-")
print(result)
#       City  Average_Age
# 0  Chicago         58.0
# 1   London         30.0
# 2    Tokyo         50.0