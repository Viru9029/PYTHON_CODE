#Q1.Write a Python program to strip a set of characters from a string. 
def strip_chr(string,char):
    return ''.join([i for i in string if i not in char])

string = input('Enter a string : ')
strip_char = input('Enter a character : ')
print(strip_chr(string,strip_char))