#!/usr/bin/python3
# key learning for data engineering or data mining:in context with sklearn lib preprocessing
# imputer is used to replace the missing data with relevent data like max min mean
# Label encoder is used to convert string data in int or float format
# OneHotEncoder is used to resolve the problem of knn type classifier (case when we are using knn then 0 value will not produce any impact on the algo) 
import pandas as pd
df=pd.read_csv("http://13.234.66.67/summer19/datasets/info.csv")
x=df.iloc[:,0:].values #greping data values only
#data label with int or float value
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
imp=Imputer(missing_values='NaN',axis=0,strategy='mean')
#df.iloc[:,1]=imp.fit_transform(df.iloc[:,1]) this give error of 2D array
impute=imp.fit(x[:,1:3]) #this is only fitting of columns that we want to process
#know time for transforming the fitted columns
x[:,1:3]=impute.transform(x[:,1:3])
count=LabelEncoder() #this is for country labeling
x[:,0]=count.fit_transform(x[:,0])
#now apply coloum first in this labelen
p=LabelEncoder()
x[:,3]=p.fit_transform(x[:,3])
#know encoding first column -----making sub column of first column
from sklearn.preprocessing import OneHotEncoder
first_column=OneHotEncoder(categorical_features=[0]) # defining exact column number where we want to make category
x=first_column.fit_transform(x).toarray() #after transformation we have to conver into numpy array
x.astype(int) #to show in int only
