#32.Write a Python program to add prefix text to all of the lines in a string.  
def add_prefix(filename,mode,prefix):
    with open(filename,mode) as file:
        lines = file.readlines()
        for i in lines:
            res = prefix+" "+i.strip()
            print(res)

filename = input('Enter the filename : ')
mode = input('Enter the filemode : ')
prefix = input('Prefix which want to enter : ')
add_prefix(filename,mode,prefix)