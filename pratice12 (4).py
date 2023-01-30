import math
a = float(input("Enter the first side of triangle : "))
b = float(input("Enter the second side of triangle : "))
c = float(input("Enter the third side of triangle : "))
semiperimeteroftriangle = (a+b+c)/2
s = semiperimeteroftriangle
areaoftriangle =math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of tringale is : %0.2f"% areaoftriangle)


