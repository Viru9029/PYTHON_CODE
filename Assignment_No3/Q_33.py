#33.	Write a Python program to set the indentation of the first line.  
def set_indentation(filename,mode):
    with open(filename,mode) as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if i == 0:
                print(lines[i].strip())
            else:
                print(lines[i],end='')


filename = input('Enter the filename : ')
mode = input('Enter the filemode : ')
set_indentation(filename,mode)