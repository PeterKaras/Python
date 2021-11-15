import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn

#Tells u number of dimensions in dataset
df.ndim

#Number of cells in dataset
df.size

#returns the type of every column
df.dtypes.values_counts()

#filter the specific type of columns
df.loc[:, (df.dtpyes == np.int64) | (df.dtypes == np.float64)]

#returns specific value
df.[price > 175]

#Multiple selecttion, ¬ negacia
df[((price > 175) & (price < 225))]

#giving the prices that are same value in brackets
df.price.isin([175,225]) -> bool
df[df.price.isin([175,225])]

#select row -> first and second row
df.iloc[[0,1]]

#select first 2 rows and first 2 columns, expecting only integers
df.iloc[[0,1],[0,1]]

#select first columns
df.iloc[,[0,1]]

#returns rows from 0 index to specific value -> 2 (including) -> only with index column
df.loc[:2]

#best practice to change value in dataframe
df.loc[df.price > 10, "Price"] = X
df.loc[(df.price > 10) & (df.value > 11), :]

#Add row 
df.loc[name] = [number of columns]

#drop specific column
#axis = 1 -> column, axis = 0 -> row
#inplace -> replace the old df
df.loc[:,df.columns.difference([columns to drop])]
df.drop(columns = [name of the columns to drop], axis = 1, inplace = True)

#drop row by index
df.drop([indexes])

#join 2 dfs, not inplace operation, join to bottom but with the axis 1 -> make new columns according to indexes
pd.concat([df1,df2])

#makes new index and the old one move as a column, but with the parameter drop=1 -> no index column
df.reset_index()

#join = outer -> common columns tell how to join these dfs
pd.concat([df1,df2], join = "outer", axis=0) # -> kluc joinovania su riadky


#join = "inner" -> only columns that dont contain of NAN, columns that are specific in both dfs
pd.concat([df1,df2], join = "inner", axis=1) # -> kluc joinovania su stlpce

#join, rsuffix -> join 2 dfs together based on the indexes that are the same in the both dfs
df1.join(df2, rsuffix = "_second") #-> left join
#how= "right" / "left"

#find NAN values
df.isna()
df.notna()

#drop NAN values
#how="all" -> drop rows with NAN value in every column
#axis = 1 -> when the column contains of NAN values, every row in the column
df.dropna()

#najpocetnejsi prvok
df.Column.value_counts.index.values[0]

#iteration
for index, row in df.iterrows():
    print()
    
df.loc[:,[columns]].apply(np.sqrt)

#separate values in specific column
df.groupby(Column)[index] #index can be N unique values in that column

#we can apply functions 
df.groupby(Column).mean()/function()[Column]

#returns dictionary of all possible states with their corresponding indexes
groupded = df.groupby(Column)
grouped.groups

#returns the values of specific state in that column
grouped.get_group("state")

#returns combinations of columns group by some columns
#as_index = False parameter -> make the columns as columns not as a index column -> if True it makes these columns as a index column
#sort = True -> sorting
df.groupby([Column,Column])

temp = df.groupby([Column,Column]).count()
temp.index

#utilize apply() function to make computation over some values column
def custom_function(grouped_df):
    return pd.Series([(grouped_df.Column + grouped_df.Column).sum(),(grouped_df.Column + grouped_df.Column).mean()], index=["SUM","MEAN"])

df.groupby([Column]).apply(custom function).to_frame()

df.groupby([Column]).apply(lambda grouped_df: pd.Series([
    (grouped_df.Column + grouped_df.Column).sum(), 
    (grouped_df.Column + grouped_df.Column).mean()], 
    index=["SUM","MEAN"]))

#CORRELATION
df.loc[:, Columns].corr()
df.cumsum(skip = "NAN")

a = np.array([[1,2,3], [4,5,6]])
np.cumsum(a) #array([ 1,  3,  6, 10, 15, 21]) 

random_matrix = np.random.randint(0,50,(4,3))
random_var = np.random.randint(0,50,N) #N - number of variables

matrix = np.matrix(([1,2],[2,3]))

df.dtpyes.values_counts()
df.set_index(Column, inplace = True)

#MISSING VALUES
pd.isna(column).notna()
df.column.isna().sum()
df.column.fillna("name_of_replacing")
df.fillna(value = 5)
df.fillna(method = "pad", limit = 1) #from top to bottom, method = "bfill" - from back to top

df.where(df > 0, -df, inplace = True)
df.apply(lambda x : x.where(x > 0, -df)) #faster

#MAKE conditions by using query
df.query("(column1 < column2) &/and (column2 < column3)")

#select type
df.select_dtypes(include = ["object"]).copy()

#Convert cat -> nums
pd.get_dummies(obj_df, columns=["drive_wheels"]).head()

df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
dataframe.col3 = pd.Categorical(dataframe.col3).codes

from sklearn.preprocessing import LabelEncoder 
labelencoder= LabelEncoder() #initializing an object of class LabelEncoder
data['C'] = labelencoder.fit_transform(data['C']) #fitting and transforming the desired categorical column.