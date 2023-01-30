# 7.	Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
# If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# def first_last_char_printer(strings):
#     if len(list(strings)) < 2:
#         print('Empty String')
#     else:
#         print(''.join(list(strings)[:2]+list(strings)[len(list(strings))-2:]))

# strings=input('Enter the string : ')
# first_last_char_printer(strings)

def first_last_char_printer(strings):
    if len(strings) < 2:
        print('Empty String')
    else:
        print(strings[:2]+strings[len(strings)-2:])

strings=input('Enter the string : ')
first_last_char_printer(strings)