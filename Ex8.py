"""Create a tuple with at least 10 elements in it
       print all elements
       perform slicing
       perform repetition with * operator
       Perform concatenation wiht other tuple.
"""

from Basics import SliceConcat, Input

print("Problem Statement:", __doc__)

tup2 = Input.fetchValidate('tuple', 1)[0]
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

str_obj = SliceConcat(tup1)
print("==============================================")
print("Printing elements of the tuple1")
str_obj.Printall()

print("\n==============================================")
str_obj.Slicing()
print("==============================================")

print("Repeating the tuple 10 times ")
str_obj.Repeat(10)
print("==============================================")

if tup2:
    print("Concatinated 2 tuples")
    str_obj.Concat(tup2)
    print("==============================================")
