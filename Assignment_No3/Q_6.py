# 6.	Write a Python program to count the number of characters (character frequency) in a string
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

def count_char(strings):
    a=[i for i in strings]
    dict_count={j:0 for j in set(a)}
    for j in a:
        dict_count[j] += 1
    print(dict_count)

strings = input('Enter the string : ')
count_char(strings)