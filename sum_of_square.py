#Sum of squares of first n natural numbers

def sum_square(n):
    sum = 0
    for i in range(1,int(n)+1):
        sum = sum+(i*i)
    print(sum)

a = float(input("Enter the natural number : "))
sum_square(a)