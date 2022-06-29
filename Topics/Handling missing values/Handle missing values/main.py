import pandas as pd

df = pd.read_csv('data/dataset/input.txt')

drop_columns = df.columns[df.isna().sum() > 7]

df.drop(drop_columns, axis=1, inplace=True)

fill_columns = df.columns[df.isna().any()]

df.fillna({c: df[c].median() for c in fill_columns}, inplace=True)

print(df.head(5))
