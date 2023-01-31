#Q14 *) Write a Python program to 
# find the first repeated character in a given string where the index of the first occurrence is smallest. 
# def find_first_repeated_char_smallest_occurrences(string):
#     dict = {i:[] for i in set(string)}
#     for i in range(len(string)):
#         for j in range(i+1,len(string)):
#             if string[i] == string[j]:
#                 dict[string[i]].append(i)
#                 dict[string[i]].append(j)
#     print(dict)

# string = input('Enter a string : ')
# find_first_repeated_char_smallest_occurrences(string)

def find_first_repeated_char_smallest_occurrences(string):
    dict = {}
    for ch in string:
        if ch in dict:
            return ch,string.index(ch)
        else:
            dict[ch] = 0

string = input('Enter a string : ')
print(find_first_repeated_char_smallest_occurrences(string))