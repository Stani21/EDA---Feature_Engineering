import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/playstore-Dataset/main/googleplaystore.csv')
print(df.head())

print(df.info())
# print(df.isnull().sum())
# print(df.describe())

print(df['Reviews'].unique())
print(df['Reviews'].str.isnumeric().sum())
non_numeric = df.loc[~df['Reviews'].str.isnumeric(),['App','Reviews']]
# print(non_numeric)

df_copy = df.copy() 
df_copy = df_copy.drop(df_copy.index[10472])

df_copy = df_copy[~df_copy['Reviews'].str.isnumeric()]
# print(df_copy.info())

df_copy = df_copy['Reviews'].astype(int)

# print(df_copy.info())
df_copy = df.copy() 
# print(df_copy['Size'].isnull().sum())

df_copy['Size'] = df_copy['Size'].str.replace('M','000')
df_copy['Size'] = df_copy['Size'].str.replace('k', '')
df_copy['Size'] = df_copy['Size'].replace('Varies with device',np.nan)
df_copy['Size'] = df_copy['Size'].str.replace('+', '', regex=False)
df_copy['Size'] = df_copy['Size'].str.replace(',', '', regex=False)
df_copy['Size'] = df_copy['Size'].astype(float)

print(df_copy.info())

# print(df_copy['Installs'].unique())
# print(df_copy['Price'].unique())

char_to_remove = ['$',',','+']
colm_to_change = ['Installs','Price']

for things in char_to_remove:
    for colm in colm_to_change:
        df_copy[colm] = df_copy[colm].str.replace(things,'')

# print(df_copy['Installs'].unique())
# print(df_copy['Price'].unique())

# print(df_copy['Installs'].unique())

# df_copy['Installs'] = df_copy['Installs'].astype(int)
# df_copy['Price'] = df_copy['Price'].astype(float)
print(df_copy.iloc[df_copy['Installs'] == 'Free'])
df_copy['Installs'] = df_copy['Installs'].str.replace('Free', '0')
df_copy['Installs']  = df_copy['Installs'].astype(int)
print(df_copy.info())


print(df_copy['Last Updated'].unique())

df_copy['Last Updated'] = pd.to_datetime(df_copy['Last Updated'],format='mixed',errors='coerce')

df_copy['Last Updated'] = pd.to_datetime(df_copy['Last Updated'])
df_copy['Day'] = df_copy['Last Updated'].dt.day
df_copy['Month'] = df_copy['Last Updated'].dt.month
df_copy['Year'] = df_copy['Last Updated'].dt.year

print(df_copy.info())

df_copy.to_csv('Cleaned_google_playstore.csv')