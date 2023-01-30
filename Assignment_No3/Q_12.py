# 12.Write a Python function that takes a list of words and return the longest word and the length of the longest one. 
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
# import functools
# def longest_word(lis_wd):
#     sep_wd = lis_wd.split(',')
#     len_count = [len(sep_wd[i]) for i in range(len(sep_wd))]
#     max_val= functools.reduce(lambda a,b : a if a > b else b,len_count)
#     max_index = [i for i in range(len(len_count)) if len_count[i] == max_val]
#     print('Longest Word : ',sep_wd[max_index[0]])
#     print('Length of Longest Word : ',max_val)




# lis_word = input('Note : Enter words by comma seperated.  Enter the words : ')
# longest_word(lis_word)

import functools
def longest_word(lis_wd):
    max_len_wd = max(lis_wd,key=len)
    max_len = functools.reduce(max,map(lambda x : len(x),lis_wd))
    print('Longest Word : ',max_len_wd)
    print('Length of Longest Word : ',max_len)




lis_word = input('Note : Enter words by comma seperated.  Enter the words : ').split(',')
longest_word(lis_word)