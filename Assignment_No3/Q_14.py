# 14.Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
def change_char(string):
    print(string[-1]+string[1:-1]+string[0])


string = input('Enter the string : ')
change_char(string)