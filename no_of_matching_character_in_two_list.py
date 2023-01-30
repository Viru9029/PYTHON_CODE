# Count the Number of matching characters in a pair of string
#
# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4
# (i.e. matching characters :- a, d, e, f)
#
# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5
# (i.e. matching characters :- b, 1, 2, @, k)

def count_no_of_matching_char_in_string(string1,string2):
    list1 = set(list(string1))
    list2 = set(list(string2))
    matching = list1 & list2
    print(len(matching))


str1 = 'abcdef'
str2 = 'defghia'
count_no_of_matching_char_in_string(str1,str2)

def count_no_of_matching_char_in_string2(string1,string2):
    list1 = list(string1)
    list2 = list(string2)
    find_word = []
    for i in list1:
        if i in list2:
            find_word.append(i)
    for j in list2:
        if j in list1:
            find_word.append(j)
    result = set(find_word)
    print(len(result))

str1 = 'abcdef'
str2 = 'defghia'
count_no_of_matching_char_in_string2(str1,str2)