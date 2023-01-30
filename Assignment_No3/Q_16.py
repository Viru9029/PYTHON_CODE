#16.Write a Python program to count the occurrences of each word in a given sentence.
def word_count(sentence):
    dict_pair = {i:0 for i in set(sentence)}
    for j in sentence:
        dict_pair[j] += 1
    print(dict_pair)

sentence = input('Enter the sentence : ').split()
word_count(sentence)