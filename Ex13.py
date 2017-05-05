"""Write a program to find the biggest of 4 numbers.
   a)  Read 4 numbers from user using Input statement.
   b) extend the above program to find the biggest of 5 numbers.
( PS : Use IF and IF & Else , If and ELIf, and Nested IF )
"""
from Basics import Input

print("Problem Statement:", __doc__)

list1 = Input.fetchValidate('list', 1)[0]

e = ''
if len(list1) == 4:
    a, b, c, d = [int(list1[0]), int(list1[1]), int(list1[2]), int(list1[3])]
elif len(list1) == 5:
    a, b, c, d, e = [int(list1[0]), int(list1[1]), int(
        list1[2]), int(list1[3]), int(list1[4])]
else:
    print("Please enter only 4 or 5 integers not more than that.")
    exit(0)


def nestif(a1, e1):
    if e1 and a1 > e1:
        print("%d is biggest number" % a1)
    elif e1 and e1 > a1:
        print("%d is biggest number" % e1)
    else:
        print("%d is biggest number" % a1)

if a > b:
    if a > c:
        if a > d:
            nestif(a, e)
        else:
            nestif(d, e)
    else:
        if c > d:
            nestif(c, e)
        else:
            nestif(d, e)
else:
    if b > c:
        if b > d:
            nestif(b, e)
        else:
            nestif(d, e)
    else:
        if c > d:
            nestif(c, e)
        else:
            nestif(d, e)
