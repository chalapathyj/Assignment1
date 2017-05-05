"""Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1.( reverse printing)
     a) By using For loop 
     b) By using while loop
    c) Let    mystring ="Hello world"
             print each character of  mystring in to separate line using appropriate  loop structure.
"""

from Basics import ForWhile, SliceConcat

string1 = "Hello World"

print("Printing elements in a while loop")
ForWhile.whileLoop(1, 100)
print("\nPrinting in reverse order using while loop:")
ForWhile.whileLoop(100, 1)
print("\nPrinting For loop")
ForWhile.forLoop(1, 100)
print("\nPrinting reverse For loop")
ForWhile.forLoop(100, -1, -1)
print("\nprinting each character of the string 'Hello World'")
SliceConcat(string1).Printall()
