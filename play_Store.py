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

df_copy = df_copy[df_copy.duplicated('App')]
df_copy = df_copy.drop_duplicates(subset=['App'], keep='first')
print(df_copy.shape)

numerical_colm = df_copy.select_dtypes(include=['number']).columns
categorical_colm = df_copy.select_dtypes(include=['object','str','category']).columns

def loopz():
    print("Numerical columns:")
    count = 0
    for i in numerical_colm:
        count = count+1
        print(i)
    print(f"Count:{count}")   

    print("Categorical columns:")
    counts = 0
    for j in categorical_colm:
        counts = counts+1
        print(j)
    print(f"counts:{counts}")
loopz()

for col in categorical_colm:
    print(df[col].value_counts(normalize=True)*100)
    print("--------------------------")

plt.figure(figsize=(15,15))
plt.suptitle("Univariate analysis of Numberical Feature",fontsize=20, fontweight='bold', alpha=0.8, y=1.)


plt.figure(figsize=(15, 15))

plt.suptitle(
    "Univariate Analysis of Numerical Features",
    fontsize=20,
    fontweight='bold',
    alpha=0.8,
    y=1.0
)

for i in range(0, len(numerical_colm)):

    plt.subplot(5, 3, i + 1)

    sns.kdeplot(
        x=df_copy[numerical_colm[i]],
        fill=True,
        color='r'
    )

    plt.xlabel(numerical_colm[i])

plt.tight_layout()
# plt.show()


plt.figure(figsize=(20,15))
plt.suptitle('Univariate Analysis of Categorical Feature', fontsize=20, fontweight='bold', alpha=0.8, y=1.)
category = ['Type','Content Rating']
for i in range(0, len(category)):
    plt.subplot(2, 2, i+1)
    sns.countplot(x=df_copy[category[i]],palette='Set2')
    plt.xlabel(category[i])
    plt.xticks(rotation=45)
    plt.tight_layout()
# plt.show()

plt.figure(figsize=(15, 17))

df_copy['Category'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Category Distribution')
plt.ylabel('')
plt.show()