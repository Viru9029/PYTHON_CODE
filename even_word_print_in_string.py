#Python program to print even length words in a string

# Input: s = "This is a python language"
# Output: This is python language

def even_word_print(string):
    split_word = string.split(" ")
    list1 = []
    for i in range(len(split_word)):
        if i % 2 == 0:
            print(split_word[i])
            #list1.append(split_word[i])
    print(list1)

s = "This is a python language"
even_word_print(s)
