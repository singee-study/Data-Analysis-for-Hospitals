import pandas as pd

pd.set_option('display.max_columns', 8)

df1 = pd.read_csv("test/general.csv")
df2 = pd.read_csv("test/prenatal.csv")
df3 = pd.read_csv("test/sports.csv")

print(df1.head(20))
print(df2.head(20))
print(df3.head(20))
