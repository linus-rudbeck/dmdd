import pandas as pd

df = pd.read_csv('Car_sales.csv')

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the first 10 rows of the DataFrame
print(df.head(10))

# Print the last 5 rows of the DataFrame
print(df.tail())

# Print the last 10 rows of the DataFrame
print(df.tail(10))

# Print information about the DataFrame
print(df.info())

# Print the shape of the DataFrame
print(df.shape)

# Print the columns of the DataFrame
print(df.columns)