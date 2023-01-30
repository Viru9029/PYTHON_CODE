# 10.	Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing', add 'ly' instead. If the string length 
# of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
def string_Change(string):
    if len(string) >= 3:
        if len(string) == 3:
            print(string+'ing')
        elif string[len(string)-3:] == 'ing':
            print(string+'ly')
    else:
        print('String less than 3 should not be changed : ',string)

string=input('Enter the string : ')
string_Change(string)