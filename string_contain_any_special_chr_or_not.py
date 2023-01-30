#Program to check if a string contains any special character


import re
def special_chr_yes_or_not(string):
    reg = re.compile('[@_!#$%^&*()<>}{":|?/]')
    if (reg.search(string)) == None:
        print("String is accepted")
    else:
        print("String is not accepted")

strings = 'Geeks For Geeks'
special_chr_yes_or_not(strings)