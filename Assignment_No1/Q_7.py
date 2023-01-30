# 7.	Accept number of rows from end user and print following * asterisk pattern ( half diamond – right )
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

def half_diamond_right_pattern(n):
    if n <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(n+1):
            print("*"*i)
        for j in range(n-1,-1,-1):
            print("*"*j)

try:
    half_diamond_right_pattern(int(input('Enter the no of rows : ')))
except:
    print('Please Enter the Integer No')