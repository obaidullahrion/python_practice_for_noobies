import pandas as pd 

df = pd.read_csv('pandas_data.csv')

# for index , row in df.iterrows():
#     print(index , row)
#print(df.loc[df['Type 2'] == 'Fire'])
# print(df.head(7).sort_values('Name' ,ascending=False))
df['Total'] = df['HP'] + df['Speed']
df = df.drop(columns=['Generation'])
print(df)