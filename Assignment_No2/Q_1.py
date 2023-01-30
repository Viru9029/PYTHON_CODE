#1.	Write a program to print 1 to 100 numbers in following table format
for i in range(1,11):
    while (i<=100):
        print('\t',i,"",end="")
        i += 10
    print()

#Q1.OR
for i in range(0,10):
    for j in range(1,101,10):
        print('\t',i+j,"",end="")
    print()

#Q1 dynamic
def print_seq_no(start,end):
    for i in range(start,start+10):
        while (i <= end):
            print('\t',i," ",end="")
            i += 10
        print()

try:
    start,end = list(map(int,input('Enter the Starting no and End no : Note : Please enter space separated values : ').split()))
    print_seq_no(start,end)
except:
    print('Please Enter Integer Value')

#Q1 dynamic
def print_seq_no(start,end):
    for i in range(0,10):
        for j in range(start,end+1,10):
            print('\t',i+j,"",end="")
        print()
try:
    start,end = list(map(int,input('Enter the Starting no and End no : Note : Please enter space separated values : ').split()))
    print_seq_no(start,end)
except:
    print('Please Enter Integer Value')