#Q16 *) Write a Python program to find the second most repeated word in a given string. 
def second_most_repeated_word(string):
    split_str = string.split()
    dict = {i:0 for i in set(split_str)}
    for i in split_str:
        dict[i] += 1
    sort_dict = sorted(dict.items(),key=lambda kv:kv[1])
    return sort_dict[-2]
string = input('Enter a string : ')
print(second_most_repeated_word(string))