# Q4). Write a Python program to print the index of a character in a string. 
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9
def character_index(string):
    a = ['current character {0} position at {1}'.format(string[i],i) for i in range(len(string))]
    for i in a:print(i,'\n')


string = input('Enter a string : ')
character_index(string)