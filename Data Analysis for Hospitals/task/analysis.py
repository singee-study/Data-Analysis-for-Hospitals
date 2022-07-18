import pandas as pd

pd.set_option('display.max_columns', 8)

df1 = pd.read_csv("test/general.csv")
df2 = pd.read_csv("test/prenatal.csv")
df3 = pd.read_csv("test/sports.csv")

df2.rename({'HOSPITAL': 'hospital', 'Sex': 'gender'}, axis=1, inplace=True)
df3.rename({'Hospital': 'hospital', 'Male/female': 'gender'}, axis=1, inplace=True)

df = pd.concat([df1, df2, df3], ignore_index=True)
df.drop(columns=['Unnamed: 0'], inplace=True)

df.dropna(axis=0, how='all', inplace=True)

df['gender'].replace({
    "female": "f",
    "woman": "f",
    "male": "m",
    "man": "m",
}, inplace=True)
df['gender'].fillna('f', inplace=True)

df.fillna(0, inplace=True)

print("The answer to the 1st question is", df.hospital.value_counts().idxmax())

df_general = df[df.hospital == 'general']
print("The answer to the 2nd question is", round(df_general.diagnosis.value_counts()['stomach'] / df_general.shape[0], 3))

df_sports = df[df.hospital == 'sports']
print("The answer to the 3rd question is", round(df_sports.diagnosis.value_counts()['dislocation'] / df_sports.shape[0], 3))

print("The answer to the 4th question is", df_general.age.median() - df_sports.age.median())

df_t = df.pivot_table(index='hospital', columns='blood_test', values='age', aggfunc='count', fill_value=0)['t']
print("The answer to the 5th question is", df_t.idxmax(), ",", df_t.max(), "blood tests")
