#30.Write a Python program to display formatted text (width=50) as output

def formatted_text(string):
    print(''.join(string))

string = input('Enter the string : ')[:50]
formatted_text(string)