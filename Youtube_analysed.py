import pandas as pd

path='E:\\All python\\Data Analysis\\Data sets\\youtube_dataset.csv'
data=pd.read_csv(path)
# print(data)

# display all rows except last 5 rows 
print(data.head(len(data)-5))
# print(data.head(-5))

# display all rows except first 5 rows 
# print(data.head(len(data.tail(len(data)-5))))
# print(data.tail(-5))

# overall statistics 
pd.options.display.float_format='{:.2f}'.format # for to get two decimal numbers after '.'
# print(data.describe())

import numpy as np
data=data.replace('--',np.nan,regex=True)
# print(data)
# print(data.isnull().sum())


import seaborn as sn 
import matplotlib.pyplot as plt

plt.figure(figsize=(5,4))
sn.heatmap(data.isnull()) 
plt.show()

# print(data.dropna(axis=0),inplace=t)

# cleaning data of Rank column
# print(data['Rank'].tail())
# data['Rank']=data['Rank'].str[0:-2]       # st,rd,th removing
# print(data['Rank'].tail())
# data['Rank']=data['Rank'].str.replace(',','')
# print(data['Rank'].tail())
# data['Rank']=data['Rank'].astype('float')
# print(data.dtypes)

# clean video upload and subscribes column 
# data['Video Uploads']=data['Video Uploads'].str.replace('--','0')
# data['Video Uploads']=data['Video Uploads'].astype('int')

# data['Subscribers']=data['Subscribers'].str.replace('--','0')
# data['Subscribers']=data['Subscribers'].astype('int')
# print(data.dtypes)

# Clean grade column 
# print(data['Grade'].unique())
# data['Grade']=data['Grade'].str.replace('\xa0','F ')
# print(data['Grade'].unique())

data['Grade']=data['Grade'].map({'A++ ':6,'A+ ':5,'A ':4,'A- ':3,'B+ ':2})
# data['Grade']=data['Grade'].map({'A++ ':6,'A+ ':5,'A ':4,'A- ':3,'B+ ':2,})
data['Grade']=data['Grade'].dropna(axis=0, inplace=True)
print(data['Grade'].unique())
# print(data['Grade'].isnull().sum())

# data['Average Views']=data['Video views']/data['Video Uploads']
# print(data.columns)
# print(data[['Average Views','Rank']])

# Find out top 5 channels with max numb of video uploads/views/Grade 

# print(data.sort_values(by=['Video Uploads'], ascending=False).head()[['Channel name','Video Uploads']])
# print(data.sort_values(by=['Video views'], ascending=False).head()[['Channel name','Video views']])
# print(data.sort_values(by=['Grade'], ascending=False).head()[['Channel name','Grade']])

# print(data.corr()) 

# which grade has max numb of video uploads 
# plt.figure(figsize=(5,4))
# sn.barplot(y='Grade',x='Video Uploads',data=data) 
# sn.scatterplot(y='Grade',x='Video Uploads',data=data) 
# sn.histplot(y='Grade',x='Video Uploads',data=data) 
# plt.show()

# which grade has highest numb of subscribers 
# plt.figure(figsize=(5,4))
# sn.barplot(y='Grade',x='Video Uploads',data=data) 
# sn.scatterplot(y='Grade',x='Video Uploads',data=data) 
# sn.histplot(x='Grade',y='Subscribers',data=data) 
# plt.show()

print(data.groupby('Grade').mean())
