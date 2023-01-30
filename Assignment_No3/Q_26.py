# 26.	Write a Python program to sort a string lexicographically.
def lexicographically_order(string):
    string.sort()
    print(' '.join(string))


string = input('Enter the string : ').split()
lexicographically_order(string)