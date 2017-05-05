""" Write a program to receive 5 command line arguments and print each argument separately.
Example :
             >> python test.py arg1 arg2 arg3 arg4 arg5
  a) From the above statement your program should receive arguments and print them each of them. 
  b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

"""
import sys
from Basics import Math

arr, arr1 = [], []
count = 0

print("Problem Statement:", __doc__)
# python <script.py> excluding <script.py>(index 0)
for x in range(1, 6):
    try:
        arr.append(int(sys.argv[x]))
    except (ValueError, IndexError) as e:
        if not IndexError:
            print("Please enter the 5 arguments along the command line")
            exit(0)
        else:
            count += 1
    try:
        arr1.append(sys.argv[x])
    except IndexError:
        print("Please pass arguments in the command line")
        exit(0)

if count <= 2:
    great_val = Math.greater(arr)
    print("Greatest among 3 numbers is ", great_val)
else:
    print("Elements passed are listed below")
    for y in arr1:
        print(y)
