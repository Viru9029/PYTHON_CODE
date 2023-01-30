#Replace duplicate Occurrence in String


# initializing string
test_str = 'Gfg is best . Gfg also has Classes now . Classes help understand better'


repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

def replace_word_in_exiting_words(string):
    convert_into_words = string.split()
    for i in range(len(convert_into_words)):
        if convert_into_words[i] in repl_dict:
            convert_into_words[i] = repl_dict.get(convert_into_words[i])
    print(convert_into_words)
    print(" ".join(convert_into_words))

replace_word_in_exiting_words(test_str)