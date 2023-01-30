# 19.	Write a Python function to create an HTML string with tags around the word(s).  
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag,string):
    print('<{0}>{1}</{2}>'.format(tag,string,tag))


tag,string = input('Note : First enter tag and then string.\nPlease enter comma seperated inputs :- \nEnter the inputs : ').split(',')
add_tags(tag,string)