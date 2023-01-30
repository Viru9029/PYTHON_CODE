#40.Write a Python program to format a number with a percentage.
def percentage_format(no):
    print('Origoinal No : {0}'.format(no))
    print('Result No : {:.2%}'.format(no))

number = float(input('Enter the number : '))
percentage_format(number)