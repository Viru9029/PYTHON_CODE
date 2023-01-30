#4.Write a program to print 11’ss table as follows
for i in range(1,11):
    for j in range(11,21):
        print('\t',i*j,end="")
    print()

#Q4.OR by horizontally
for i in range(11,21):
    j = 1
    while (i <= 200 and j <= 10):
        print('\t',i*j,end="")
        j += 1
    print()

