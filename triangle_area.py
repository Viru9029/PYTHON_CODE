#calculate area of triangle
a = float(input())
b = float(input())
c = float(input())

#semiperimetr
semi = (a+b+c)/2

area_of_triangle = (semi * (semi-a) * (semi-b) * (semi-c)) ** 0.5

print(area_of_triangle)