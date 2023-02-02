# Q2.*) Write a Python program to count repeated characters in a string. 
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
def count_char(string):
    initial_char = {i:0 for i in set(string)}
    for i in string:
        initial_char[i] += 1
    print(initial_char)


string = input('Enter a string to count characters : ')
count_char(string)