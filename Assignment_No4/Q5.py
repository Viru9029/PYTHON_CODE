#Q5) Write a Python program to check whether a string contains all letters of the alphabet. 
def check_alpha_string(string):
    if string.isalpha():
        return True
    else:
        return False


string = input('Enter a string : ')
print(check_alpha_string(string))