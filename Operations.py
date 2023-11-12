n = (1+2)*2/3
print ("BODMAS - ",n)

r = 11%3
print ("Remainder - ",r)

square = 2**2
cube = 2**3
fourth = 2**4
print(square, cube, fourth)

string = "Younu" + "<3" + "Hallu"
print(string)

stringmul = "HaNu " * 7
print(stringmul)

e = [2,4,6,8] #Can't Mention datatype for list
o = [1,3,5,7]
eo = e + o
oe = o + e
#eeo = e - o #Can't multiply non-int (error)
#muleo = e * o #Can't multiply non-int (error)
#muloe = o * e
print("Even+Odd : ",eo)
print("Odd+Eveb : ",oe)
#print("Even-Odd : ",eeo)
#print("Even*Odd : ",muleo)
#print("Odd*Eveb : ",muloe)

listmul = [2,5,8] * 2
print(listmul)

#Exercise 
x = object()
y = object()

xlist = [x] * 10
ylist = [y] * 10
blist = xlist + ylist
print("X list has %d objects(variable)" % len(xlist))
print("X list objects are : ", xlist)
print("Y list has %d objects(variable)" % len(ylist))
print("Y list objects are : ", ylist)
print("Big list has %d objects(variable)" % len(blist))
print("Big list objects are : ", blist)

if xlist.count(x) == 10 and ylist.count(y) == 10:
    print("10 x objects in X list and 10 y objects in Y list")
if blist.count(x) == 10 and blist.count(y) == 10:
    print("10 x objects in Big list and 10 y objecta in B list as added")
