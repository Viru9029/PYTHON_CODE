# 8.Write a Python program to get a string from a given string where all occurrences of its first char have been 
# changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
# def char_replace(string):
#     a = ''.join(['$' if list(string)[0] == list(string)[i] else list(string)[i] for i in range(len(string))])
#     print(list(string)[0]+a[1:])


# string=input("Enter the String : ")
# char_replace(string)

def char_replace(string):
    a = ''.join(['$' if string[0] ==string[i] else string[i] for i in range(len(string))])
    print(string[0]+a[1:])


string=input("Enter the String : ")
char_replace(string)