import pandas as pd
dict1 ={'Name':['Zain','Kasaf','Zeenat','Ali','Umer',
                'Ishal','Mehwish'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }
df1=pd.DataFrame(dict1)
# print(df1.head(3))
# print(df1.head())
# print(df1.tail())
# print(df1.shape) 
# print("Number of rows in dataset: ",df1.shape[0]) #0 index for rows
# print("Number of columns in dataset: ",df1.shape[1]) 

# general overview of dataset column and total rows 
# print(df1.info())

# find is there any null value or not  
# print(df1.isnull())

# find overall description/information of dataset 
# print(df1.describe(include='all'))

# find unique values from any colummn 
# print(df1['Gender'].unique())

# Find number of unique values from gender  
# print(df1['Gender'].nunique()) # This method can be used to with dataframe also 

# display count of unique values in any column (gender) 
# print(df1['Gender'].value_counts())

# find total number of students having marks>=90 and less then 99
# print(df1[df1['Marks']>=90])
# print(df1[ (df1['Marks']>=90) & (df1['Marks']<99)] )
# print(len(df1[ (df1['Marks']>=90) & (df1['Marks']<99)] ) )

# showing with between method  
# print(sum(df1['Marks'].between(90,99) )) #this is including 99 value also like <=
# print(sum(df1['Marks'].between(90,98) ))

# find name of stud having low marks 
print(df1[df1['Marks'].min() == df1['Marks']]['Name'])

# find average/max/min of marks 
# print(df1['Marks'].mean())
# print(df1['Marks'].max())

# Add new column 
def marks(x):
    return  x//2 # floor division to cut 0 
# df1['Half Marks']=df1['Marks'].apply(marks)
# print(df1)

# Add new colum using lambda function 
# df1['Half Marks']=df1['Marks'].apply(lambda x:x//2)
# print(df1)

# Change male/female to 0,1 and add new cloumn 
# df1['Male_Female']=df1['Gender'].map({'Male':1,'Female':0})
# print(df1)

# to delete column 
# df1.drop('Male_Female',axis=1,inplace=True)

# if any row have all missing values then delet that one
# df1.dropna(how='all',axis=0,inplace=True)
# print(df1)

# For multiple columns deletions 
# df1.drop(['Male_Female','Half Marks'],axis=1,inplace=True)
# print(df1)

# find name of columns 
# print(df1.columns)

# sort data according to marks 
# print("\n             Assending order data")
# print(df1.sort_values(by='Marks'))
# print("\n             Descending order data")
# print(df1.sort_values(by='Marks',ascending=False))
# print(df1.sort_values(by=["Gender",'Marks']))

# show male students records
# print(df1[df1['Gender']=='Male'])

# show name  and marks of male students 
# print(df1[df1['Gender']=='Male'][['Name','Marks']])

# show name of the students having marks>=90
# print(df1[df1['Marks']>=90]['Name'])

# replace/fill missing values 
# df1['Marks']=df1['Marks'].fillna(df1['Marks'].mean())
# print(df1['Marks'])

# to check null values in columns 
# print(df1.isnull().sum())

# to check null values in rows 
# print(df1.isnull().sum(axis=1))

# def marks(x):
#     return x+" Awon"

# print(df1['Name'].apply(marks))
# print(df1['Name'].apply(lambda x:x+" Awon"))

# find top 5 students name in class (any numb of rows)
# print(df1.nlargest(5,'Marks')[['Name','Marks']])

# rename column 
# df1.rename(columns={'Marks':'Final_Marks','Email':'New_email'})
 
# merge two data sets 
# dict2 ={'Name':['Babar'],
#                 'Marks':[98],
#                 'Gender':['Male']
#                }
# df2=pd.DataFrame(dict2,index=[0])

# df3=pd.concat([df1,df2],ignore_index=True)
# print(df3)

# loc & iloc to select particular row/column (order/index of columns matter)

# labels used in loc function 
# print(df1.loc[:,'Marks':'Gender'])

# indexes use in iloc function 
# print(df1.iloc[:,1:3])
print(df1.iloc[0,0:3])