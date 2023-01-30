import re


def spliting_string_from_vowels(str):
    a = re.split('a|e|i|o|u', str)
    print(a)


test_str = 'GFGaBste4oCS'
spliting_string_from_vowels(test_str)
