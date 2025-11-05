import pandas as pd

import os
print("Current working directory:", os.getcwd())

df = pd.read_csv("netflix.csv")

#Operations
print("First 5 Records: ")
print(df.head())

print("Last 5 records: ")
print(df.tail())

print("Total Number of Rows and Columns: ")
print(df.shape)

print("Column: ")
print(df.columns)

print(df.describe())

print('--------------------------')
print(df.info)


print('--------------------------')
series = df['Release_Year']

# top 5 data
print(series.head())

# bottom 5 data
print(series.tail())


print(series.shape)

print(series.describe())
