# Replace all occurrences of a substring in a string
#
# Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd”
#
# Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str.
#
# Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd”


def replace_substring(string,string_word,replace_word):
    find_word_in_string = string.split(string_word)
    print(find_word_in_string)
    str = ""
    for i in find_word_in_string:
        if i == '':
            str += replace_word
        else:
            str += i

    print(str)


test_str = 'geeksforgeeks'
s1 = 'geeks'
s2 = 'abcd'
replace_substring(test_str,s1,s2)