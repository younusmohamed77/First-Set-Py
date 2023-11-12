class Vehicle: #Definition of class
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle() #Object for car 1
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle() #Object for car 2
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())

#Same using functions
def fun_description (name, kind, colour, value):
    print ("%s is a %s %s worth $%.2f" % (name, kind, colour, value))

fun_description ("Fer", "red", "convertible", 60000.00)
fun_description ("Jump", "blue", "van", 10000.00)

