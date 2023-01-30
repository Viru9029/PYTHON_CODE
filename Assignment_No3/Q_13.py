# 13.	Write a Python program to remove the nth index character from a nonempty string.
def remove_char(string,index_no):
    if string[0].isalpha() == True:
        print(string[:index_no]+string[index_no+1:])
    else:
        print('String is Empty.Please Enter the string.')


string,index_no=input('Note:Enter details by using space seperated.  Enter the string : ').split(',')
remove_char(string,int(index_no))