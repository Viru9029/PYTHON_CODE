# Find words which are greater than given length k
#
# Input : str = "hello geeks for geeks
#           is computer science portal"
#         k = 4
# Output : hello geeks geeks computer
#          science portal
# Explanation : The output is list of all
# words that are of length more than k.
#
# Input : str = "string is fun in python"
#         k = 3
# Output : string python

def greater_len_word_accepted(strings,len_word_accepted):
    list2 = strings.split()
    res = []
    for i in range(len(list2)):
        if len(list2[i]) > len_word_accepted:
            print(list2[i], end=" ")
            #res.append(list2[i])


str1 = "hello geeks for geeks is computer science portal"
greater_len_word_accepted(str1,5)

