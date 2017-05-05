# for problem 1,9
class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return (self.a + self.b)

    def sub(self):
        return (abs(self.a - self.b))

    def mul(self):
        return (self.a * self.b)

    def div(self):
        try:
            return (self.a / self.b)
        except ZeroDivisionError:
            return ("not possible because divider is 0")

    # for problem 2,5,17
    @staticmethod
    def greater(list_of_num):
        max = 0
        for x in list_of_num:
            x = int(x)
            if (x > max):
                max = x
        return max

# problem 3_4_16


class PrimeOdd:

    def __init__(self, a):
        self.a = a

    def prime(self):
        i = 2
        while(i <= (self.a / 2)):
            if(self.a % i == 0):
                return "not a prime number"
                break
            i += 1
        else:
            return "is a prime number"

    def odd_even(self):
        return "even" if(self.a % 2 == 0) else "odd"

# problem 6,7,8, 14


class SliceConcat:

    def __init__(self, a):
        self.a = a

    def Printall(self):
        for x in self.a:
            print(x, end=' ')

    def Slicing(self):
        i = 1
        print("few substrings are")
        while(i < len(self.a)):
            print(self.a[0:i])
            i += 1

    def Repeat(self, count=5):
        if type(self.a) is tuple:
            print((self.a) * count)
        elif type(self.a) is list:
            print([self.a] * count)
        elif type(self.a) is str:
            print((self.a + ", ") * count)

    def Concat(self, datatyp2):
        print(self.a + datatyp2)


class ModExpFlr(Math):

    def __init__(self, a, b):
        super(ModExpFlr, self).__init__(a, b)

    def mod(self):
        return self.a % self.b

    def exp(self):
        return self.a ** self.b

    def flr(self):
        return self.a // self.b

# problem 17, 18 and 15


class ForWhile:

    def forLoop(a, b, c=1):
        # addinc c parameter to print the array in reverse using -1
        for x in range(a, b + 1, c):
            print(x, end=' ')

    def whileLoop(a, b, brkval=0):
        """2 while loops one for fwd looping and onother for reverse.
           at the end of fwd looping a is greater than b so it enters b.
           to stop that the a value is decremented and exits the loop.
        """

        if not brkval:
            brkval = b
        while a <= b:
            print(a, end=' ')
            if a == brkval:
                a -= 1
                break
            a += 1

        while a >= b:
            print(a, end=' ')
            a -= 1
