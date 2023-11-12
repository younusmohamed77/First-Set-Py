#Print all even numbers in the same order
#Don't print any number after 237
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

#  Using for loop
for i in numbers: # For loop works in range not in condition
    if (i == 237): # Not to print any number after 237
        break # Will terminate and exit the loop
    if (i%2 == 1): # To check if even Number
        continue # Will break abd return to looping (to demonstrate continue)
    print (i)
    if (i%2 == 0): # Same without continue
        print (i)

# Same using while loop
j = 0
while True:
    if (numbers[j] == 237):
        break
    if (numbers[j]%2 == 0):
        print(numbers[j])
    j += 1
    
# Else for loop
for i in numbers:
    while i%2 == 0:
        print("%d is Even" % i)
        break # Terminates and exits inner while loop
    else: # Else condition for while loop
        print("%d is Odd" % i)
