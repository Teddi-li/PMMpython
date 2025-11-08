import pandas as pd

df = pd.read_csv('sales.csv')
print(df.head())
print(df['price'].mean())
grouped = df.groupby('category')['sales'].sum()
print(grouped)
