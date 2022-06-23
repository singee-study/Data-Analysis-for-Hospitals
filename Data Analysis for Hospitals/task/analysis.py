import pandas as pd

pd.set_option('display.max_columns', 8)

df1 = pd.read_csv("test/general.csv")
df2 = pd.read_csv("test/prenatal.csv")
df3 = pd.read_csv("test/sports.csv")

df2.rename({'HOSPITAL': 'hospital', 'Sex': 'gender'}, axis=1, inplace=True)
df3.rename({'Hospital': 'hospital', 'Male/female': 'gender'}, axis=1, inplace=True)

df = pd.concat([df1, df2, df3], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)

print(df.sample(n=20, random_state=30))
