# 8) Write a Python program to swap commas and dots in a string. 
# Sample string: "*)*),*)
# Expected Output: "*)*).*)
def swap_commas(string):
    return string.replace(',','.')

string = input('Enter a string : ')
print(swap_commas(string))