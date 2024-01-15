import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path="E:\\All python\\Data Analysis\\Data sets\\IMDB-Movie-Dataset.csv"
data=pd.read_csv(path)
# print(data)

# drop missing Values 
# print(data.isnull().sum())
# print(data.dropna(axis=0, inplace=True))
# print(data.isnull().sum())

# movies title having runtime>=180
# print(data[data['Runtime (Minutes)']>=180][['Title','Runtime (Minutes)']])

# in which year there was the highest average voting 
# print(data.groupby('Year')['Votes'].mean().sort_values(ascending=False).head(1))

# bar plot is best to use when one variable is integer type and other is catagorical 
# in which year there was the highest average voting 
# sns.barplot(x='Year',y='Votes',data=data)
# plt.show()
 
# in which year there was the highest average Revenue 
# print(data.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False).head(1))
# sns.barplot(x='Year',y='Revenue (Millions)',data=data)
# sns.boxenplot(x='Year',y='Revenue (Millions)',data=data)
# sns.histplot(data)
# plt.show()

# Average rating for each director 
# print(data.groupby('Director')['Rating'].mean().sort_values(ascending=False))
# print(data.groupby('Genre')['Rating'].mean().sort_values(ascending=False))

# find top 10 lengthy movies title and runtime 
# print(data.nlargest(10,'Runtime (Minutes)')[['Title','Runtime (Minutes)']])

# print(data['Year'].value_counts())
# sns.histplot(data['Year'])
# sns.countplot(x='Year', data=data)
# plt.show()

# display title of highest revenue generated movie 
# print(data.groupby('Revenue (Millions)')['Rating'].mean().sort_values(ascending=False))
# print(data[data['Revenue (Millions)'].max()==data['Revenue (Millions)']]['Title'])

# diplay top 10 highest rated movie title and its directors 
# print(data.nlargest(10,'Rating')[['Title','Runtime (Minutes)']].set_index('Title'))

# t10=data.nlargest(10,'Rating')[['Title','Director','Rating']].set_index('Title')    
# print(data.nlargest(10,'Rating')[['Title','Director','Rating']].set_index('Title'))

# visualize now 
# plt.figure(figsize=(10,5))
# sns.barplot( x='Rating', y=t10.index, data=t10, hue='Director')
# sns.countplot( x='Rating', data=t10, hue='Director' ,dodge=False)

# #to make directors box outside of main box 
# plt.legend(bbox_to_anchor=(1.05,1),loc=2)
# plt.show()

# Top 10 highest revenue movie titles 
# t10=data.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)','Rank']].set_index('Title')
# print(t10)  

# sns.barplot( y='Revenue (Millions)', x=t10.index, data=t10, hue='Rank')
# plt.xticks(rotation=60)
# plt.show()

# average rating of movies year wise 
# print(data.groupby('Year')['Rating'].mean())

# Does rating affect revenue 
# sns.scatterplot(x='Rating',y='Revenue (Millions)',data=data)
# plt.show()

# Classify movies based on Ratings 

# def rat(rating):
#     if rating>=7.0:
#         return "Excellent"
#     elif rating>=5.0:
#         return "Good"
#     else:
#         return "Average"
# data['New_Rating']=data['Rating'].apply(rat)
# print(data)
# print(data['New_Rating'].value_counts())

# count numb of action movies 
# print(len(data[data['Genre'].str.contains('Action')]))

# print(data['Genre'])
# data['New Genre']=data['Genre'].str.replace(',',' ')

# find unique genre 
# list1=[]
# for value in data['Genre']:
#     list1.append(value.split(','))
# # print(list1)
# one_d=[]
# for item in list1:
#     for item1 in item:
#         one_d.append(item1)
# uni_list=[]
# for item in one_d:
#     if item not in uni_list:
#         uni_list.append(item)
# print(uni_list) 

# how many fulms of each genre were made


list1=[]
for value in data['Genre']:
    list1.append(value.split(','))

one_d=[]
for item in list1:
    for item1 in item:
        one_d.append(item1)
from collections import Counter 

print(Counter(one_d))