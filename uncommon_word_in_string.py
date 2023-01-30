# Python program to find uncommon words from two Strings
#
# Input : A = "Geeks for Geeks"
#         B = "Learning from Geeks for Geeks"
# Output : ['Learning', 'from']
#
# Input : A = "apple banana mango"
#         B = "banana fruits mango"
# Output : ['apple', 'fruits']

def uncommon_words_in_string(string1,string2):
    dictionay = {}
    for word1 in string1.split():
        dictionay[word1] = dictionay.get(word1,0) + 1

    for word2 in string2.split():
        dictionay[word2] = dictionay.get(word2,0) +1

    print(dictionay)
    res = [i for i in dictionay if dictionay[i] == 1]
    print(res)


A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
uncommon_words_in_string(A,B)