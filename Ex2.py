"""Write a program to find the biggest of 3 numbers ( Use If Condition )
"""
from Basics import Math, Input

print("Problem Statement:", __doc__)

list_of_num = Input.fetchValidate('int', 3)
great_val = Math.greater(list_of_num)

print("Greatest among 3 integers is ", great_val)
