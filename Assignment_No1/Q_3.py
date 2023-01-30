# 3.	Accept number of rows from end user and print following * asterisk pattern ( inverted right-angle triangle )
# *****
# ****
# ***
# **
# *

def inverted_right_angle_triangle_pattern(n):
    if n <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(0,n+1):
            print('*'*(n-i))

try:
    inverted_right_angle_triangle_pattern(int(input('Enter the number of rows : ')))
except:
    print('Please Enter the Integer No')