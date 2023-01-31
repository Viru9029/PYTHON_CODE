#18) Write a Python program to move spaces to the front of a given string. 
def move_spaces(string):
    no_spac_chr = ''.join([i for i in string if i != ' '])
    total_space = len(string) - len(no_spac_chr)
    print(' '*total_space + no_spac_chr)

string = input('Enter a string : ')
move_spaces(string)