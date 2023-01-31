#20) Write a Python program to capitalize the first and last letters of each word in a given string.
# def first_last_word_capital(string):
#     lis = []
#     for i in range(len(string)):
#         for j in range(len(string[i])):
#             if j == 0 or j == len(string[i])-1:
#                 string[i][j] == string[i][j].upper()
#             # else:
#             #     lis.append(string[i][j])
#     print(' '.join(string))


# string = input('Enter a string : ').split()
# first_last_word_capital(string)

def first_last_word_capital(string):
    string = string.title()
    result = ''
    for word in string.split():
        result += word[:-1] + word[-1].upper() + ' '

    print(result)



string = input('Enter a string : ')
first_last_word_capital(string)
