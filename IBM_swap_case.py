def swap_case(a,b):
    a,b = b,a
    print('a = {0} , b = {1}'.format(a,b))

a = 10
b = 20
swap_case(a,b)


##OR

def swap_case2(a,b):
    a = b
    b = a
    print('a = {0} , b = {1}'.format(a,b))

a = 30
b = 40
swap_case(a,b)


##OR

def swap_case3(a,b):
    temp = a
    a = b
    b = temp

    print('a = {0} , b = {1}'.format(a,b))

a = 50
b = 60
swap_case3(a,b)