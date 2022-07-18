import pandas as pd

df = pd.read_csv('data/dataset/input.txt')

print(round(df.pivot_table(index='labels')['null_deg']['R'], 2))
