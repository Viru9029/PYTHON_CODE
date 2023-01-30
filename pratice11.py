a = 7/3
print(a)
print("\r") #2.333333335

b = 7//3
print(b)
print("\r") #2

c = -7/3
print(c)
print("\r") #-2.333333335

d = -7//3
print(d)
print("\r") #-3

e = 7//-3
print(e)
print("\r") #-3

f = 2.25/265.3263
print(f)
print("\r") #0.008480124284701516

g = 2.25//265.3263
print(g)
print("\r") #0.0

f = 5+2j
h = 8+6j
print(f+h)
print("\r")#(13+8j)

m = complex(8, 6)
print(m)
print("imag value : ", m.imag)
print("real value : ", round(m.real))
print("\n") #(8+6j)
            #imag value :  6.0
            #real value :  8

n = 5+2J
o = 8+3J
print(n+o)
print("\n") #(13+5j)

p = 5.0+9.0j
#float(p) #The conversion functions to floating point and integer (float(), int() and
# long()) don’t work for complex numbers — there is no one correct way to convert
# a complex number to a real number.
print(p.real, p.imag)
#print(p)
q = abs(p)#abs gives only positive value output
print(q)
print("\n")

r = -65895
s = 110.12
t = 56598
print("{0} , {1} , {2}".format(abs(r), abs(s), abs(t))) #abs gives only positive value output
print("\n")#65895 , 110.12 , 56598

width = 20
height = 5*9
i = width * height
print(i)
print("\r")#900

j = k = l = 0
print(" j = {0}, k = {1}, l = {2}" .format(j, k, l))
print("\n")# j = 0, k = 0, l = 0

import math
print(math.ceil(125.32), "\n")
print(math.floor(125.32), "\n")
print(math.ceil(125.56), "\n")
print(math.floor(125.56), "\n")
print(math.ceil(-125.56), "\n")
print(math.floor(-125.56), "\n")
print("\n")

u =input("Enter the numbers : ")
list = u.split(",")
tuple = tuple(list)
print("Max no is : ", max(tuple))
print("Min no is : ", min(tuple))
print("\n")


v = pow(2,2)
w = math.pow(5,2)
print(v,w)
print("\n")#4 , 25.0

print(round(125.5, 0))#126.0
print(round(125.5, 1))#125.5
print(round(125.5, 2))#125.5
print(round(125.5, 3))#125.5
print(round(125.5, -1))#130.0
print(round(125.5, -2))#100.0
print(round(125.5, -3))#0.0
print("\n")

import cmath
print(math.sqrt(25))#5.0
print(cmath.sqrt(25))#(5+0j)
print("\n")

