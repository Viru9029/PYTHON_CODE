#5.Write a program to print 21’s table as follows

for i in range(1,11):
    for j in range(21,31):
        print('\t',i*j,end="")
    print()

#Q5.OR by horizontally
for i in range(21,31):
    j = 1
    while (i <= 300 and j <= 10):
        print('\t',i*j,end="")
        j += 1
    print()

