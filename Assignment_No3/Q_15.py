#15.	Write a Python program to remove characters that have odd index values in a given string.
def remove_odd_chr(string):
    return ''.join([string[i] for i in range(len(string)) if i % 2 == 0])
    
string = input('Enter the string : ')
print(remove_odd_chr(string))