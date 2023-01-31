# 7) Write a Python program to lowercase the first n characters in a string. 
def lowercase_nth_char(string,n):
    print(''.join(string[:n].lower()+string[n:].upper()))


string = input('Enter a String : ')
nth = int(input('Enter the first n characters : '))
lowercase_nth_char(string,nth)