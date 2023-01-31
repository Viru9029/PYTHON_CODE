#19) Write a Python program to find the maximum number of characters in a given string. 
def max_char_in_string(string):
    dict = {i:0 for i in set(string) if i != ' '}
    for i in string:
        if i in dict:
            dict[i] += 1
    print(max(zip(dict.values(),dict.keys())))

string = input('Enter a string : ')
max_char_in_string(string)