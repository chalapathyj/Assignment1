"""Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.
"""
from Basics import Input

print("Problem Statement:", __doc__)

int1, int2 = Input.fetchValidate('int', 2)

print("AND operator: The value of %d and %d is " % (int1, int2), int1 & int2)
print("OR operator: The value of %d or %d is " % (int1, int2), int1 | int2)
print("XOR operator: The value of %d xor %d is " % (int1, int2), int1 ^ int2)
print("Compliment operator: The complement value of %d is " % (int1), ~int1)
print("Left shift operator: %d left shifted by %d is " %
      (int1, int2), int1 << int2)
print("Right shift operator: %d right shifted by %d is " %
      (int1, int2), int1 >> int2)
