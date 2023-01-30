#ArmStrong number program
import math
number = int(input("Enter the number : "))
a = number % 10
print(a)
b = (number // 10) % 10
print(b)
c = (number // 100) % 10
print(c)
d = math.pow(a,3)
e = math.pow(b,3)
f = math.pow(c,3)
sum = d+e+f
print(sum)
if sum == number:
    print("It is ArmStrong number")
else:
    print("Not an ArmStrong number")