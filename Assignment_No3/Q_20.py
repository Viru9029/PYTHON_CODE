# 20.	Write a Python function to insert a string in the middle of a string.  
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_string_middle(style,string):
    s = style
    print(s[:int(len(s)/2)]+string+s[int(len(s)/2):])

style,string = input('Note : First enter Style and then String.\nPlease enter comma seperated inputs :- \nEnter the inputs : ').split(',')
insert_string_middle(style,string)