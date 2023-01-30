#34.Write a Python program to print the following numbers up to 2 decimal
def two_decimal_no(no):
    print('Original No : {0}'.format(no))
    print('Result No : {:.2f}'.format(no))


number = float(input('Enter the number : '))
two_decimal_no(number)