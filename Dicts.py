#First Method
phonebook = {}
phonebook["A"] = 938477566
phonebook["B"] = 938377264
phonebook["C"] = 947662781
print(phonebook)

#Second method
#If we do this the pevious one will be delted
phonebook = {
    "D" : 938477566,
    "E" : 938377264,
    "F" : 947662781
}
print(phonebook)

#But we can add items to dicts as below (1st Method)
phonebook["A"] = 938477566
phonebook["B"] = 938377264
phonebook["C"] = 947662781
print(phonebook)

#We can use for loop, but it will not follow any order
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#To delete a value
del phonebook["A"]
print(phonebook)

#To celete second method
phonebook.pop("B")
print(phonebook)

