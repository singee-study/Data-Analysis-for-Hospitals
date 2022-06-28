import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

print((df.isnull().sum() / df.shape[0]).round(2))