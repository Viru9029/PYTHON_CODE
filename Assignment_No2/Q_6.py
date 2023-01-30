#6.Write a program to dynamically accept range ( two integers ) and print table chart for given range

#Q6 BY FOR LOOP
def make_table(start,end):
    for i in range(1,11):
        for j in range(start,end+1):
            print('\t',i*j,end=" ")
        print()


try:
    start,end = list(map(int,input('Enter the starting no and End no Note : Write space separated values : ').split()))
    make_table(start,end)
except:
    print('Please Enter Integer Value')

#Q6 BY WHILE LOOP print horizontally
def make_table(start,end):
    for i in range(start,end+1):
        j = 1
        while (i <= end) and (j <= 10):
            print('\t',i*j,end=" ")
            j += 1
        print()


try:
    start,end = list(map(int,input('Enter the starting no and End no Note : Write space separated values : ').split()))
    make_table(start,end)
except:
    print('Please Enter Integer Value')

