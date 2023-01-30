#24.	Write a Python function to reverse a string if its length is a multiple of 4.  
def reverse_str(string):
    if len(string) % 4 == 0:
        print(string[::-1])
    else:
        print(string)


string = input('Enter the string : ')
reverse_str(string)