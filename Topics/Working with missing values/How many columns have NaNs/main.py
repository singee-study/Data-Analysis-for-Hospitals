import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

cdf = df.isna().sum()

print(cdf[cdf != 0].count())
