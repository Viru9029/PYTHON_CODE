# 6.	Accept number of rows from end user and print following * asterisk pattern ( full diamond )
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *

def diamnond_pattern(n):
    if n <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(n):
            print(" "*(n-i),"*"*(2*i+1))
        for j in range(n-2,-1,-1):
            print(" "*(n-j),"*"*(2*j+1))

try:
    diamnond_pattern(int(input('Enter the number of rows : ')))
except:
    print('Please Enter the Integer No')