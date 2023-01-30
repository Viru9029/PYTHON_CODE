# 10.	Accept number of rows from end user and print following * asterisk pattern
#   *******
#    *****
#     ***
#      *
#     ***
#    *****
#   *******
def half_half_diamond_pattern(n):
    if n <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(n-1,-1,-1):
            print(" "*(n-i),"*"*(2*i+1))
        for j in range(1,n):
            print(" "*(n-j),"*"*(2*j+1))

try:
    half_half_diamond_pattern(int(input('Enter the no of rows : ')))
except:
    print('Please Enter the Integer No')