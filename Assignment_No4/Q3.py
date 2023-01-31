# Q3. Write a Python program to print the square and cube symbols in the area of a rectangle and the volume of a cylinder. 
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
def area_volume(area,volume,decimal):
    print("The area of the rectangle is : {0:.{1}f}cm\u00b2".format(area,decimal))
    print("The volume of the cylinder is : {0:.{1}f}cm\u00b3".format(volume,decimal))


area = float(input('Enter the area of the rectangle is : '))
volume = float(input('Enter the volume of the cylinder is : '))
decimal = int(input('Enter the decimal point : '))
area_volume(area,volume,decimal)