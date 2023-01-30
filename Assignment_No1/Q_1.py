# #1.	Accept number of rows from end user and print * asterisk on each row. E.g. if input is 5 then
# *
# *
# *
# *
# *


def print_asterisk(user_input):
    if user_input <= 0:
        return print('Please Enter Positive No')
    else:
        for i in range(0,user_input):
            print('*')


try:
    print_asterisk(int(input('Enter the number of rows : ')))
except:
    print('Please Enter the Integer No')