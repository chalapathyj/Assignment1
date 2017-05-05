class Input:

    def intTypeCast(n):
        try:
            a = int(n)
        except ValueError:
            print("Please try again by entering an integer")
            exit(0)
        return a

    def fetchValidate(datatype, end):
        list1 = []
        count = 1
        for x in range(1, end + 1):
            s = datatype + str(count)
            y = input("Enter the value for %s: " % s).strip()
            if datatype == 'int':
                list1.append(Input.intTypeCast(y))
            elif datatype == 'tuple':
                list1.append(tuple(y.split(' ')))
            elif datatype == 'list':
                list1.append(y.split(' '))
            else:
                list1.append(y)
            if not y:
                print("Please enter the value")
                exit(0)
            count += 1

        return list1
