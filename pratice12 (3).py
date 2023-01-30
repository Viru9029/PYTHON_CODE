import math
a = int(input("Enter the integer number : "))
squarroot = math.sqrt(a)
print("square root of {0} is : {1}".format(a, squarroot))
print("square root of %0.2d is : %d"% (a, squarroot))
print("\n")

b = float(input("Enter the float number : "))
squarroot1 = math.sqrt(b)
print("square root of ", b, "is : ", squarroot1)
print("\n")

c = float(input("Enter the number : "))
squareroot2 = c ** 0.5
print("square root of ",+float(c),"is : ",+float(squareroot2))