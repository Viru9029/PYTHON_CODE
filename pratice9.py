n = int(input("Enter the number : "))
n1 = int("%s" %n)
n2 = int("%s%s" %(n, n))
n3 = int("%s%s%s" %(n, n, n))
sum = n1 + n2 +n3
print("Sum : ", sum)