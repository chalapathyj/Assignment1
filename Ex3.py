""" Write a program to find  given number is odd or Even
"""

from Basics import PrimeOdd, Input

print("Problem Statement:", __doc__)

a = Input.fetchValidate('int', 1)

obj1 = PrimeOdd(a[0])

print("The number '%s' is " % a[0], obj1.odd_even())
