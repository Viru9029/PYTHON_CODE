# 28.	Write a Python program to check whether a string starts with specified characters. 
import string
def check_start_string_spec_chr(strings):
    if strings[0] in string.punctuation:
        print('String start with specified character.')
    else:
        print('String not start with specified character')

strings = input('Enter the string : ')
check_start_string_spec_chr(strings)