import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

print(list(df.isna().any()).count(True))
