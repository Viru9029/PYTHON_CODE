# 5.Accept number of rows from end user and print following * asterisk pattern (( inverted equilateral triangle ))
# *******
#  *****
#   ***
#    *

def inverted_equilateral_trangle_pattern(n):
    if n <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(n,-1,-1):
            print(" "*(n-i),"*"*(2*i+1))

try:
    inverted_equilateral_trangle_pattern(int(input('Enter the no of rows : ')))
except:
    print('Please Enter the Integer No')