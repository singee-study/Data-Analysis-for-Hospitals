import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

old_count = df.shape[0]

ndf = df.dropna(axis=0)

new_count = ndf.shape[0]

print(old_count, new_count)

