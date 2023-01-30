#27.	Write a Python program to remove a newline in Python. 

def remove_newline(strings):
    print(' '.join(strings.split('\\n')))
    #print(string.replace('\\n',' '))



string = input('Note : To Enter multiline input Please use \'\\n\' \nEnter the lines :  ')
remove_newline(string)