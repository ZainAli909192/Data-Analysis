import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path="E:\\All python\\Data Analysis\\Data sets\\Forest_fire_dataset.csv"
data = pd.read_csv(path, encoding='latin-1',parse_dates=['date'])

print(data.columns)
# print(data.dtypes)

# print(data.head())
# print(data.tail(5))

# print(data.shape)
# print(data.duplicated().any() )
# data=data.drop_duplicates()
# print(data.shape)

# find null values 
# print(data.isnull().sum())

# which year/month has max numb of fires reported 
# print(data.columns)
# print(data.groupby('year')['number'].max().sort_values(ascending=False)) 
# print(data.groupby('month')['number'].max().sort_values(ascending=False)) 

# visualize it 
# sns.barplot(x='year',y='number',data=data, hue='year')
# sns.barplot(x='month',y='number',data=data, hue='month')
# plt.show()

# in which state max numb fires registers 
# print(data.groupby('state')['number'].sum().sort_values(ascending=False))

# sns.barplot(x='state',y='number',data=data, hue='state')
# plt.xticks(rotation=60)
# plt.show()

# numb of fires in amazonas state 
# print(data['state']=='Amazonas'.sum())
# print(data[data['state']=='Amazonas'][['number','month','state']])

# numb of fires  reported in Amazonas (Year wise ) 
# print(data[data['state']=='Amazonas'][['number','month','state']].sum() )
# data1=data[data['state']=='Amazonas']
# data2=data1.groupby('year')['number'].sum()
# print(data2)

# numb of fires reported in Amazonas day-wise 
# data3=data[data['state']=='Amazonas']
# print(data3.dtypes)
# print(data3.groupby(data3['date'].dt.day_of_week).sum())

# find total numb of fires reported in 2015 
# print(len(data[data['year']==2015]))

# data4=data[data['year']==2015]
# sns.barplot(x='year', y='month',data=data4)
# sns.countplot(data4['month'])
# plt.show()

data5=data[data.groupby('state')['number'].mean().sort_values(ascending=False)]
# print(data5)

sns.barplot(x='state',y='number', data=data5)
plt.show()










