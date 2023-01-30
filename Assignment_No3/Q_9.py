# 9.	Write a Python program to get a single string from two given strings, separated by a space and swap 
# the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
# def swap_first_two_char(string):
#     sep = string.split(',')
#     if len(sep) % 2 == 0:
#         print(sep[1][:2]+sep[0][2:]," ",sep[0][:2]+sep[1][2:])
#     else:
#         print('Enter the string which is divisible by 2 ')

# string=input('Note:Please Enter comma seperated strings.  Enter the String : ')
# swap_first_two_char(string)

def swap_first_two_char(string):
    sep = string.split(',')
    a = [print(sep[i+1][:2]+sep[i][2:]," ",sep[i][:2]+sep[i+1][2:]) if len(sep) % 2 == 0 else print('Enter the string which is divisible by 2 ') for i in range(0,len(sep),2)]

string=input('Note:Please Enter comma seperated strings.  Enter the String : ')
swap_first_two_char(string)