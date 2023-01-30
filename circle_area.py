#area of circle
#formula = pie * r square

import math
radius = float(input("Enter the radius of circle : "))
def area_of_circle(radius):
    pi = math.pi #or 3.14
    area = pi * (radius*radius)
    print(area)

area_of_circle(radius)