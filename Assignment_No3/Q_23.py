# 23.	Write a Python program to get the last part of a string before a specified character 
def lst_part_str(string,spec_chr):
    print(string.rsplit(spec_chr, 1)[0])


string,spec_chr = input('Note : First enter string and then enter spec.character. \nPlease enter space seperated values \nEnter the inputs : ').split()
lst_part_str(string,spec_chr)
