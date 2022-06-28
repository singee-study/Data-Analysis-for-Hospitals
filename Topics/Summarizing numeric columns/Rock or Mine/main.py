import pandas as pd

df = pd.read_csv("data/dataset/input.txt")

m = df[df['labels'] == 'M']['null_deg'].median()
r = df[df['labels'] == 'R']['null_deg'].median()

print("M = {:.3} R = {:.3}".format(m, r))
