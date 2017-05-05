"""Write a program to create two list A and B such that List A contains Employee Id, List B contains Employee name
     ( minimum 10 entries in each list ) and perform following operations
     a) Print all names on to screen
     b) Read the index from the  user and print the corresponding name from both list.
     c) Print the names from 4th position to 9th position
     d) Print all names from 3rd position till end of the list
     e) Repeat list elements by specified number of times ( N- times, where N is entered by user)
     f)  Concatenate two lists and print the output.
     g) Print element of list A and B side by side.( i.e.  List-A First element ,  List-B First element )

"""

from Basics import SliceConcat, Input

print("Problem Statement:", __doc__)

arg1, arg2 = Input.fetchValidate('int', 2)

empid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
empname = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

id_obj = SliceConcat(empid)
name_obj = SliceConcat(empname)

print("Printing all employee names: ")
name_obj.Printall()

print("\n-------------------------------------------------")
print("The employee id and name for the index %d is " %
      arg1, "id: ", empid[arg1], " name:", empname[arg1])

print("-------------------------------------------------")
print("The employee names from 4 to 9 are ", empname[3:9])

print("-------------------------------------------------")
print("The employee names from 3 till end ", empname[2:])
print("-------------------------------------------------")

print("Repeating the employee ids by %d " % arg1)
id_obj.Repeat(arg1)
print("-------------------------------------------------")

print("Repeating the employee names by %d " % arg1)
name_obj.Repeat(arg1)
print("-------------------------------------------------")

print("Concatinated list of employee ids and names")
id_obj.Concat(empname)
print("-------------------------------------------------")

print("Printing employee id and name side by side")
for x, y in zip(empid, empname):
    print(x, ":", y)
print("-------------------------------------------------")
