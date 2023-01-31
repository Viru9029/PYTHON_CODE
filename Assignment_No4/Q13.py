#Q13) Write a Python program to find the first repeated character in a given string. 
def first_repeated_char(string):
    for i in range(len(string)):
        if string[i] in string[i+1:]:
            return string[i]
    else:
        print('No any repeated character found.')


string = input('Enter a string : ')
print(first_repeated_char(string))