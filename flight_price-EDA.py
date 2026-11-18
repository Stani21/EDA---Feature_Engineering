# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("shubhambathwal/flight-price-prediction")

# print("Path to dataset files:", path)

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('business.csv')
# print(df.head())
df['Date'] = df['date'].str.split('-').str[0]
df['Month'] = df['date'].str.split('-').str[1]
df['Year'] = df['date'].str.split('-').str[2]
# print(df.head())

df['Date'] = df['Date'].astype(int)
df['Month'] = df['Month'].astype(int)
df['Year'] = df['Year'].astype(int)
df.info()

df.drop('date',axis=1,inplace=True)
# print(df.head())

df['Arraival_Minute'] = df['arr_time'].str.split(":").str[0]
df['Arraival_Hour'] = df['arr_time'].str.split(":").str[1]
print(df.head())

df['stop'] = df['stop'].str.replace(r'\s+', ' ', regex=True).str.strip()
# print(df['stop'].unique())
# print(df['stop'].mode())
print(df['stop'].value_counts())

df['stop'] = df['stop'].map({'non-stop':0,'1-stop':1,'2+-stop':2,'np.nan':1})
print(df['stop'].isnull())
print(df['stop'].value_counts())

print(df.head())
df['time_taken_hrs'] = df['time_taken'].str[:2]
df['time_taken_mins'] = df['time_taken'].str[4:6]
print(df['time_taken_mins'])
# print(df['time_taken_hrs'])
print(df['airline'].unique())

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder()
print(encoder.fit_transform(df[['airline','ch_code','num_code']]).toarray())

print(pd.DataFrame(encoder.fit_transform(df[['airline','ch_code','num_code']]).toarray(),columns=encoder.get_feature_names_out()))

# df.info()
# print(df.describe())

