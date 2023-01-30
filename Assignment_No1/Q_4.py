# 4.	Accept number of rows from end user and print following * asterisk pattern ( equilateral triangle )
#     *
#    ***
#   *****
#  *******

def equilaterial_triangle_pattern(n):
    if n <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(n):
            print(" "*(n-i),"*"*(2*i+1))

try:
    equilaterial_triangle_pattern(int(input('Enter the number of rows : ')))
except:
    print('Please Enter the Integer No')