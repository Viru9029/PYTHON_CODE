# 18.	Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in
# sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
def sorted_alphabates(lis_word):
    lis_word.sort()
    #print(sorted(lis_word))
    print(lis_word)


lis_wd = input('Enter the by using comma seperated : ').split(',')
sorted_alphabates(lis_wd)