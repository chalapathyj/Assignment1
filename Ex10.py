""" Using assignment operators, perform following operations
    Addition, Substation, Multiplication, Division, Modulus, 
    Exponent and Floor division operations
"""

from Basics import ModExpFlr, Input

print("Problem Statement:", __doc__)

int1, int2 = Input.fetchValidate('int', 2)

if not int1 or not int2:
    print("Enter the value(s)")
    exit(0)

obj1 = ModExpFlr(int1, int2)

print("Addition of %d and %d is " % (int1, int2), obj1.add())
print("Subtraction of %d and %d is " % (int1, int2), obj1.sub())
print("Multiplication of %d and %d is " % (int1, int2), obj1.mul())
print("Division of %d by %d is " % (int1, int2), obj1.div())
print("Modulus of %d by %d is " % (int1, int2), obj1.mod())
print("%d Exponent of %d is " % (int1, int2), obj1.exp())
print("Floor division of %d by %d is " % (int1, int2), obj1.flr())
