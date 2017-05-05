#import cmath

"""Write program to Add , subtract, multiply, divide 2 complex numbers.
"""

from Basics import Math, Input

print("Problem Statement:", __doc__)

cn1, cn2 = Input.fetchValidate('str', 2)
op = input("Enter the operation 'add' or 'sub' or 'mul' or 'div': ").strip()

obj1 = Math(complex(cn1), complex(cn2))

if op == "add":
    print("Addition of two numbers is ", obj1.add())
if op == "sub":
    print("Subtraction of two numbers (absolute) is ", obj1.sub())
if op == "mul":
    print("Multiplication of two numbers is ", obj1.mul())
if op == "div":
    print("Division of two numbers is ", obj1.div())
