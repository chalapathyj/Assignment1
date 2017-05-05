"""Write program to find  the biggest  and Smallest of N numbers.
      PS: Use the functions to find biggest and  smallest numbers. 
"""
from Basics import Math, Input

print("Problem Statement:", __doc__)

list1 = Input.fetchValidate('list', 1)[0]

great_val = Math.greater(list1)
print("Greatest among integers is ", great_val)


def smaller(l1):
    min = great_val
    for y in l1:
        y = int(y)
        if y < min:
            min = y
    return min

small_val = smaller(list1)
print("Smallest among the integers is ", small_val)
