
def fine_location_of_word_in_string(st,word):
    split_word = st.split()
    index_no = ""
    for i in range(len(split_word)):
        if split_word[i] == word:
            index_no += str(i+1)
    print(index_no)
    print(type(index_no))




str1 = 'geeksforgeeks is best for geeks'
find_word = 'best'
fine_location_of_word_in_string(str1,find_word)