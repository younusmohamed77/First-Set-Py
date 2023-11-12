#Exercise
#First, convert the list of weights from a list to a Numpy array.
#Then, convert all of the weights from kilograms to pounds.
#Use the scalar conversion of 2.2 lbs per kilogram to make your conversion.
#Lastly, print the resulting array of weights in pounds.

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

print(weight_kg)
for i in weight_kg:
    print ("Weight in kgs is %.2f kg" %i)

np_weight_kg = np.array(weight_kg)
print(np_weight_kg)
for i in weight_kg:
    print ("Weight in kgs array is %.2f kg" %i)

np_weight_lbs = np_weight_kg * 2.2
print(np_weight_lbs)
for i in np_weight_lbs:
    print ("Weight in pounds array is %.2f lbs" %i)

i=0
while i<len(np_weight_kg):
    print ("%.2f kgs =" %np_weight_kg[i], "%.2f lbs" %np_weight_lbs[i])
    print ("%.2f kgs = %.2f lbs" %(np_weight_kg[i],np_weight_lbs[i]))
    i+=1
