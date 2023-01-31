#Q11.Write a Python program to find the first non-repeating character in a given string. 
def find_first_non_repeating_char(string):
    for i in range(0, len(string)):
        if string[i] not in string[i+1:]:
            return string[i]
    else:
        return None

string = input('Enter a String : ')
print(find_first_non_repeating_char(string))

    # for i in range(len(string)):
    #     for j in range(i+1, len(string)):
    #         if string[i]!= string[j]:
    #             return string[i]
    # return None