# word_list = ["best", 'CS', 'for']

# # initializing replace word
# repl_wrd = 'gfg'


def replace_word(str, word_list, replace_wd):
    dictonary = {}
    new_str = []
    for i in word_list:
        dictonary[i] = replace_wd
    for j in str.split():
        if j in dictonary:
            new_str.append(dictonary.get(j))
        else:
            new_str.append(j)
    print(dictonary)
    print(" ".join(new_str))


word_list = ["best", 'CS', 'for']
repl_wrd = 'gfg'
test_str = 'Geeksforgeeks is best for geeks and CS'
replace_word(test_str, word_list, repl_wrd)
