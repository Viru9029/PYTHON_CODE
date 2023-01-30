#Check if a given string is binary string or not

# Input: str = "01010101010"
# Output: Yes
#
# Input: str = "geeks101"
# Output: No

def string_binary_or_not(strings):
    unique_words_in_string = list(set(strings))
    print(unique_words_in_string)
    if unique_words_in_string == (['0','1'] or ['1','0']):
        print("String is Binary")
    else:
        print("String is NOT Binary")


str = "geeks101"
string_binary_or_not(str)