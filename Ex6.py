"""Write a program to read string and print each character separately.
    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
    b) Repeat the string 100 times using repeat operator *
    c) Read strig 2 and  concatenate with other string using + operator.
"""

from Basics import SliceConcat, Input

print("Problem Statement:", __doc__)

str1, str2 = Input.fetchValidate('str', 2)

str_obj = SliceConcat(str1)
print("==============================================")
print("Printing each character of string1 seperately")
str_obj.Printall()

print("\n==============================================")
str_obj.Slicing()
print("==============================================")
cl
print("Repeating the string 100 times")
str_obj.Repeat(100)
print("==============================================")

if str2:
    print("Concatinated string 1 and 2")
    str_obj.Concat(str2)
    print("==============================================")
