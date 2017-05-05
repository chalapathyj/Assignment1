"""Read 10 numbers from user and find the average of all.
a) Use comparison operator to check how many numbers are less than average and print them
b) Check how many numbers are more than average.
c) How many are equal to average.
"""

from Basics import Input

print("Problem Statement:", __doc__)

list1 = Input.fetchValidate('list', 1)[0]

sum1, count = 0, 0

for x in list1:
    x = int(x)
    sum1 += x
    count += 1
average = int(sum1 / count)
print("Average of the integers is %d" % average)
eq_avg, gt_avg, lt_avg = 0, 0, 0

for x in list1:
    x = int(x)
    if x > average:
        gt_avg += 1
    elif x < average:
        lt_avg += 1
    else:
        eq_avg += 1

print("Values greater than average is %d" % gt_avg)
print("Values less than average is %d" % lt_avg)
print("Values greater than average is %d" % eq_avg)
