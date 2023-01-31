#17)Write a Python program to remove spaces from a given string.
# def remove_spaces(string):
#     return ''.join(string.split())

# string = input('Enter a string : ')
# print(remove_spaces(string))

#OR

# def remove_spaces(string):
#     return string.replace(' ','')

# string = input('Enter a string : ')
# print(remove_spaces(string))

#OR
def remove_spaces(string):
    return ''.join(string)

string = input('Enter a string : ').split()
print(remove_spaces(string))