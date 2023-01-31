#Q15)Write a Python program to find the first repeated word in a given string
def first_repeated_word_in_string(string):
    split_string = string.split()
    for i in range(len(string)):
        if split_string[i] in split_string[i+1:]:
            return print('First repeated char : ',split_string[i])
    else:
        return print('No any repeated word found.')


string = input('Enter a string : ')
first_repeated_word_in_string(string)