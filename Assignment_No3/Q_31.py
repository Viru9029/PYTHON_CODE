#Write a Python program to remove existing indentation from all of the lines in a given text 
def remove_identation(filename,mode):
    with open(filename,mode) as file:
        lines = file.readlines()
        for i in lines:
            pri = i.strip()
            print(pri)


filename = input('Enter the filename : ')
mode = input('Enter the filemode : ')
remove_identation(filename,mode)
