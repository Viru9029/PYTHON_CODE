import sys
flag = True
while flag:
    try:
        s = 3
        b = 0
        a = 15
        l = 6
        d = a / b
        c = [1,2,3]
        e = c[l]
        f = s + c
        flag = False

    except(ZeroDivisionError,IndexError,TypeError):
        t = sys.exc_info()[1]
        if str(t) == "division by zero":
            print(sys.exc_info()[1])
            b = 1
        elif str(t) == "list index out of range":
            print(sys.exc_info()[1])
            l = 2
        elif str(t) == "unsupported operand type(s) for +: 'int' and 'list'":
            print(sys.exc_info()[1])
