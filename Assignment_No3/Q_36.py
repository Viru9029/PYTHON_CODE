#36.Write a Python program to print the following positive and negative numbers with no decimal places 
def no_decimal_number(no):
    print('Original No : {0}'.format(no))
    print('Result No : {:+.0f}'.format(no))


number = float(input('Enter the number : '))
no_decimal_number(number)