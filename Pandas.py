dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }
#Dict is a keyword to mention dict
#We can put anyname (like br=..)
#While calling we can use use 'dict' or 'br' both will work

import pandas as pd
#DataFrame is the key Data Structure in Date Manipulation using Pandas
#Pandas was built using Numbey arrays
#DataFrames allow you to store and manipulate tabular data
#in rows of observations and columns of variables. 
brics = pd.DataFrame(dict)
print(brics)
print(dict)
#print(brics[0]) Cannot call using index like this

#Set the index (first column data) for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

#Import the cars.csv data: cars
#cars = pd.read_csv('cars.csv')
#Not able to import the file for now

#To print one column use column name as index
#Print as data series
print(brics['area'])
#Print as datafarame use another square brackets
print(brics[['area']])
#We can add more column to dataframes
print(brics[['area','country']])

#we can use square brackets to print rows also (using row number)
print(brics[0:5])
print(brics[1:5])
print(brics[2:5])   
print(brics[3:5])
print(brics[4:5])
print(brics[5:5])#Empty DataFrame

#loc is used to access data using labels(row and column name)
#iloc is used to access data using integer index
print(brics.iloc[3])
print(brics.loc[['area','country']])
