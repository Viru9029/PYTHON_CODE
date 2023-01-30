#35.Write a Python program to print the following numbers up to 2 decimal places with a sign 
def decimal_with_sign(no):
    print('Original No : {0}'.format(no))
    print('Result No : {:+.2f}'.format(no))

number = float(input('Enter the number : '))
decimal_with_sign(number)