#Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

#b = weight / (height ** 2)
#TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

#Import the numpy package as np
import numpy as np

#Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(height)
print(np_height)
print(weight)
print(np_weight)

#We have type
print(type(np_height))

#BMI
bmi = np_weight / (np_height ** 2)
print(bmi)

#Checking with index
chkind = np_weight[0] / (np_height[0] ** 2)
print(chkind)
print(bmi[0])
#Indices work fine

#Rounding float
round(chkind,2)#This is a command only
print(round(chkind,2))
chkind = (round(chkind,2))
print(chkind)

#Subsetting (checking) with a condition
print(bmi < 25) #This will print only boolean (True or False)
print(bmi[bmi < 25]) #This will print all values below 25
print(bmi[bmi < 25][0]) #This will print the first value below 25
print(bmi[bmi < 25][1]) #This will print second value below 25
#print(bmi[bmi < 25][2])
#IndexError: index 2 is out of bounds for axis 0 with size 2
#print(round(bmi[bmi < 25],2)) Cannot round off like this
#print(round(bmi[bmi < 25][0]),2)
#print(round(bmi[bmi < 25][1]),2)
