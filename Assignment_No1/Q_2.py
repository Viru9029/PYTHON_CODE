# 2.	Accept number of rows from end user and print following * asterisk pattern ( right angle triangle )
# *
# **
# ***
# ****
# *****

def right_angle_triangle_pattern(n):
    if n <= 0:
        return print('Please Enter Positive No')
    else:
        for i in range(0,(n+1)):
            print('*'*i)

try:
    right_angle_triangle_pattern(int(input('Enter the number of rows : ')))
except:
    print('Please Enter the Integer No')