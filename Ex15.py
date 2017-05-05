"""Create a list of 5 names and check given name exist in the List.
        a) Use membership operator ( IN ) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction.
        List elements are ['perl', 'python', 'tcl', 'java', 'c']
"""
from Basics import Input

print("Problem Statement:", __doc__)

arg1 = Input.fetchValidate('str', 1)[0]

names = ['perl', 'python', 'tcl', 'java', 'c']

if arg1 in names:
    print("Element found using IN operator")
else:
    print("Element not found, used IN operator")

for y in range(0, 5):
    if names[y] == arg1:
        print("Element found using '==' operator")
        break
else:
    print("Element not found, used '==' operator")

print("Printing the array in reverse")
for z in range(4, -1, -1):
    print(names[z])
