# Write a program which will accept ‘N’ number from user and print 1 through ‘N’ numbers in table format in batch of 100’s.
#  e.g if user enters 1000 then create 10 tables of 10X10 size ( 1 through 100, 101 through 200, 201 through 300 …. So on )
#Q2.while loop
def print_seq_no(end):
    for i in range(1,11):
        while (i <= end):
            print('\t',i," ",end="")
            i += 10
        print()

try:
    end= int(input('Enter the Starting no and End no : Note : Please enter space separated values : '))
    print_seq_no(end)
except:
    print('Please Enter Integer Value')

#Q.2 OR column wise
def print_seq_no(end):
    for i in range(0,10):
        for j in range(1,end+1,10):
            print('\t',i+j," ",end="")
        print()

try:
    end= int(input('Enter the Starting no and End no : Note : Please enter space separated values : '))
    print_seq_no(end)
except:
    print('Please Enter Integer Value')

#Q2 Or row Wise
def print_seq_no(end):
    for i in range(1,end+1,10):
        for j in range(0,10):
            print('\t',i+j," ",end="")
        print('\n')

try:
    end= int(input('Enter the Starting no and End no : Note : Please enter space separated values : '))
    print_seq_no(end)
except:
    print('Please Enter Integer Value')

#Q.2 OR by using module operator
def print_seq_no(end):
    count = 1
    for i in range(1,end+1):
        if i % 100 == 1:
            print('\n','Table No : ',count)
            count += 1
            
        print(i,end='\t')
        
        if (i%10) == 0:
            print()

try:
    end= int(input('Enter the End No : '))
    print_seq_no(end)
except:
    print('Please Enter Integer Value')

#Q.2 OR column wise
def print_seq_no(end):
    for i in range(0,10):
        for j in range(1,end+1,10):
            print('\t',i+j," ",end="")
        print()

try:
    end= int(input('Enter the Starting no and End no : Note : Please enter space separated values : '))
    print_seq_no(end)
except:
    print('Please Enter Integer Value')