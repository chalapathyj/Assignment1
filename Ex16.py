"""Write program to perform following:
     i) Check whether given number is prime or not.
    ii) Generate all the prime numbers between 1 to N where N is given number.
"""
from Basics import PrimeOdd, Input

print("Problem Statement:", __doc__)

int1, int2 = Input.fetchValidate('int', 2)

prim_obj = PrimeOdd(int1)

print("The number %d " % int1, prim_obj.prime())
print("The prime numbers from 2 to %d are " % int2)

if int2 <= 1:
    print("No prime numbers")
for x in range(2, int2 + 1):
    # prime numbers are greater than 1
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                break

        else:
            print(x, end=' ')
