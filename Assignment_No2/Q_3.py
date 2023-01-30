#3.	Write a program to print following 2’s table

for i in range(1,11):
    for j in range(1,11):
        print('\t',i*j,end="")
    print()

#Q.3 OR
for i in range(1,11):
    j = 1
    while(i<=100 and j <= 10):
        print('\t',i*j,end="")
        j += 1
    print()

