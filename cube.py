def sum_of_cube(n):
    sum = 0
    for i in range(1,int(n+1)):
        sum = sum + (i*i*i)
    print(sum)

a = float(input("Enter the any Natural Number : "))
sum_of_cube(a)