import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

mean = round(df.groupby('location')['height'].transform('mean'), 1)

df['height'] = df['height'].fillna(mean)

print(df['height'].sum())



