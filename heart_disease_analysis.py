import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path="E:\\All python\\Data Analysis\\Data sets\\heart_dataset.csv"
data = pd.read_csv(path, encoding='latin-1')

# print(data)

# print(data.head(5))
# print(data.tail(5))

print(data.shape)
# print(data.info)
# print(data.isnull().sum())

print(data.duplicated().value_counts())
# print(data.duplicated().sum())
# data_dup=data.duplicated().any()
# print(data_dup)
data=data.drop_duplicates()
# print(data.shape)

# print(data.describe())

# print(data.corr())

# sns.heatmap(data.corr())
# plt.show()

# how many people have heart disease and how many not
# print(data.columns) 
# print(data['target'].value_counts()) 

# which gender has the most heart diseases 
# print(data.groupby('target')['sex'].value_counts())

# sns.histplot(data['target'])
# plt.show()

# find count of male and female 
# print(data['sex'].value_counts())

# print(data.groupby('sex')['target'].value_counts())

# sns.histplot(data['sex'])
# sns.countplot(x='sex',data=data,hue='target')
# plt.xticks([1,0],['Male','Female'])
# plt.show()

# print(data['age'].value_counts())
# sns.countplot(x='age',data=data,hue='age')
# sns.distplot(data['age'])
# plt.show()

# find types of chest pain 
# print(data.columns)
# print(data['cp'].unique())

# how many patients in each chest pain 
# print(data['cp'].value_counts())
# sns.distplot(data['cp'],bins=20)
# plt.show()

# how many peole having chest pain and also having heart disease 
# print(data.groupby('cp')['target'].value_counts())

# sns.barplot(x='cp' , y='target',data=data, hue='cp')
# plt.show()

# print(data.groupby('fbs')['target'])

# sns.countplot(x='fbs' , y='target',data=data, hue='cp')
# sns.countplot(x='fbs' ,data=data, hue='target')
# plt.xticks([0,1],['Diseased','No heart diseases'])
# plt.show()

# Check Resting Blood Pressure Distribution

# sns.countplot(x='trestbps' ,data=data, hue='target')
# plt.hist(data['trestbps'])
# plt.xticks(rotation=60)
# plt.show()

# Compare Resting Blood Pressure As Per Sex Column
# sns.countplot(x='trestbps' ,data=data, hue='sex')
# plt.hist(data['trestbps'])
# plt.xticks(rotation=60)
# plt.show()

# compare resting blood pressure as per sex 
# g=sns.FacetGrid(data,hue='sex',aspect=3)
# g.map(sns.kdeplot,'trestbps',shade=True)
# plt.legend(labels=['Male','Female'])
# plt.show()

# Show Distribution of Serum cholesterol
# data['chol'].hist()
# plt.show()

# Plot Continuous Variables
cate_val=[]
cont_val=[]

for column in data.columns:
    if data[column].nunique()<=10:
        cate_val.append(column)
    else :
        cont_val.append(column)

# data[cont_val].hist()
data[cate_val].hist()
plt.tight_layout()
plt.show()




