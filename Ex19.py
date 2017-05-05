"""Using loop structures print even numbers between 1 to 100.
     a) By using For loop , use continue/ break/ pass statement to skip  odd numbers.
           i)  break the loop if the value is 50
           ii) Use continue for the values 10,20,30,40,50

     b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
            i)  break the loop if the value is 90
           ii) Use continue for the values 60,70,80,90

"""


def forloop(l1=[], brk=0):
    for x in range(1, 101):
        if x % 2 != 0:
            continue
        print(x, end=' ')
        if x in l1 and brk:
            break
        if x in l1:
            continue


def whileloop(l1=[], brk=0):
    i = 2
    while i <= 100:
        if i % 2 != 0:
            i += 1
            continue
        print(i, end=' ')
        if i in l1 and brk:
            break
        if i in l1:
            i += 1
            continue
        i += 1

print("Skipping odd numbers in the range of 1 to 100 using for loop: ")
forloop()
print("\nBreaking the loop if the value is 50")
forloop([50], brk=1)
print("\nContinue the range if the value is 10, 20, 30, 40, 50")
forloop([10, 20, 30, 40, 50])

print("\nSkipping odd numbers in the range of 1 to 100 using while loop: ")
whileloop()
print("\nBreaking the loop if the value is 90 using while loop")
whileloop([90], brk=1)
print("\nContinue the range if the value is 60, 70, 80, 90")
whileloop([60, 70, 80, 90])
