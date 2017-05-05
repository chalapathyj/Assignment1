"""Create a list with at least 10 elements in it
       print all elements
       perform slicing
       perform repetition with * operator
       Perform concatenation wiht other list.
"""

from Basics import SliceConcat, Input

print("Problem Statement:", __doc__)

lst2 = Input.fetchValidate('list', 1)[0]
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

str_obj = SliceConcat(lst1)
print("==============================================")
print("Printing elements of the list1")
str_obj.Printall()

print("\n==============================================")
str_obj.Slicing()
print("==============================================")

print("Repeating the list 10 times ")
str_obj.Repeat(10)
print("==============================================")

if lst2:
    print("Concatinated List")
    str_obj.Concat(lst2)
    print("==============================================")
