# 11.	Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def change_substring(string,substring1,substring2):
    sep_word = string.split()
    lis = []
    for i in range(len(sep_word)):
        if (sep_word[i] == substring1 and sep_word[i+1] == substring2) or (sep_word[i] == substring1 and sep_word[i+2] == substring2):
            lis.append('good!')
            break
        else:
            lis.append(sep_word[i])
    print(' '.join(lis))


string = input('Enter the string : ')
substring1 = 'not'
substring2 = 'poor!'
change_substring(string,substring1,substring2)