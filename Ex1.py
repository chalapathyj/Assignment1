"""Write a program to add , Subtract, Multiply, and divide 2 numbers
"""
from Basics import Math, Input

print("Problem Statement:", __doc__)

int1, int2 = Input.fetchValidate('int', 2)
op = input("Select the operation 'add' or 'sub' or 'mul' or 'div': ").strip()

obj1 = Math(int1, int2)

if op == "add":
    print("Addition of two numbers is ", obj1.add())
if op == "sub":
    print("Subtraction of two numbers (absolute) is ", obj1.sub())
if op == "mul":
    print("Multiplication of two numbers is ", obj1.mul())
if op == "div":
    print("Division of two numbers is ", obj1.div())
