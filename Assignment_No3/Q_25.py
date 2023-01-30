# 25.	Write a Python function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters 
def if_first_chr_upper(string):
    count = 0
    for i in range(0,4):
        if string[i] == string[i].upper():
            count += 1
    if count >= 2:
        print(string.upper())
    else:
        print('Two character are not in UPPERCASE')


string = input('Enter the string : ')
if_first_chr_upper(string)