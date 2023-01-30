# Python program for removing i-th character from a string
#
# g
# e
# e
# k
# s
# 0
# 1
# 2
# 3
# 4
# Examples:
#
# Input: Geek
# i = 1
# Output: Gek
#
# Input: Peter
# i = 4
# Output: Pete

def remove_ith_no_chr_from_string(strings,i):
    if i <= (len(strings)):
        first = strings[:i]
        second = strings[i+1:]
        final = first + second
        print(final)
    else:
        print("Enter the valid index")


stri = 'Geek'
remove_ith_no_chr_from_string(stri,3)