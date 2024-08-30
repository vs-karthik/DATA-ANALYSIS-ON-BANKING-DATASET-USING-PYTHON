

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('banking_data.csv', encoding='unicode_escape')


'''sns.histplot(df['age'], bins=20)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()'''

'''plt.figure(figsize=(10, 6))
df['job'].value_counts().plot(kind='bar')
plt.title('Distribution of Job Types')
plt.xlabel('Job Type')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()'''

'''plt.figure(figsize=(8, 6))
df['marital'].value_counts().plot(kind='bar')
plt.title('Distribution of Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.show()'''

'''plt.figure(figsize=(8, 6))
df['education'].value_counts().plot(kind='bar')
plt.title('Distribution of Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.show()'''


'''value= df['default'].value_counts().unique()
total = value[0] + value[1]
proportion = value[1]/total
print(f'proprotion of clients having credit in default (in percentage): {proportion}')'''

'''plt.figure(figsize=(8, 6))
sns.histplot(df['balance'], bins=20)
plt.title('Distribution of Average Yearly Balance')
plt.xlabel('Balance')
plt.ylabel('Count')
plt.show()'''

'''housing_loan = df["housing"].value_counts().unique()

print(f'The number of clients with housing loan {housing_loan[1]}')'''

'''print("Communication types used for contacting clients:")
print(df['contact'].unique())'''


plt.figure(figsize=(8, 6))
df['day_month'].value_counts().plot(kind='bar')
plt.title('Distribution of Last Contact Day of the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Count')
plt.show()

'''plt.figure(figsize=(8, 6))
df['month'].value_counts().plot(kind='bar')
plt.title('Distribution of Last Contact Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.show()'''

'''plt.figure(figsize=(8, 6))
sns.histplot(df['duration'], bins=20)
plt.title('Distribution of Last Contact Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Count')
plt.show()'''

'''print(f"Number of contacts performed during the campaign: {df['campaign'].unique()}")'''

'''plt.figure(figsize=(8, 6))
sns.histplot(df['pdays'], bins=20)
plt.title('Distribution of Days Since Last Contact')
plt.xlabel('Days')
plt.ylabel('Count')
plt.show()'''

'''print(f"Number of contacts performed before the current campaign: {df['previous'].unique()}")'''

'''print("Outcomes of the previous marketing campaigns:")
print(df['poutcome'].unique())'''

'''values = df['y'].value_counts().unique()
not_subscribed = values[0]
subscribed = values[1]
total_clients = not_subscribed + subscribed

proportion_of_not_subscribed = not_subscribed/total_clients*100

proprotion_of_subscribed = subscribed/total_clients*100

print(f'proportion of clients not subscribed to term deposit (in percentage) : {proportion_of_not_subscribed}')

print(f'proprotion of clients subscribed to term deposit (in percentage) : {proprotion_of_subscribed}')'''

'''numeric_df = df.select_dtypes(include=['int64','float64'])
corr_matrix = numeric_df.corr()
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix,annot=True,cmap='PuBuGn',fmt=".2f")
plt.title("Correlation of banking dataset")
plt.show'''


