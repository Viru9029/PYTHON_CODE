#Words Frequency in String Shorthands

# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
#
# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

def word_freq_count(sentence):
    split_sentence = sentence.split()
    unique_words_in_sentense = list(set(split_sentence))

    count = []
    for i in range(len(unique_words_in_sentense)):
        count.append(0)

    dictionary = dict(zip(unique_words_in_sentense,count))

    for i in range(len(split_sentence)):
        if split_sentence[i] in dictionary.keys():
            dictionary[split_sentence[i]] += 1
        else:
            continue
    print(dictionary)

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
word_freq_count(test_str)