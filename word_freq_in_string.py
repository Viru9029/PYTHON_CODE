# Words Frequency in String Shorthands

# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}

# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

def count_word_in_string(str):
    split_word = str.split()
    unique_words = set(split_word)
    dictionary = {}
    for i in range(len(split_word)):
        if split_word[i] in dictionary:
            dictionary[split_word[i]] = dictionary.get(split_word[i],0)+1
        else:
            dictionary[split_word[i]] = dictionary.get(split_word[i],0)+1
    print(dictionary)


test_str = 'Gfg Gfg Gfg'
count_word_in_string(test_str)