#Q10.) Write a Python program to split a string on the last occurrence of the delimiter. 
# def split_delimiter_string(string,delimiter,occurrences):
#     return string.split(delimiter)[-occurrences:]


# string = input('Enter a string : ')
# delimiter = input('Enter delimiter string : ')
# occurrences = int(input('Enter the number of occurrences: '))
# print(split_delimiter_string(string,delimiter,occurrences))


#OR

def split_delimiter_string(string,delimiter,occurrences):
    return string.rsplit(delimiter,occurrences)[1:]


string = input('Enter a string : ')
delimiter = input('Enter delimiter string : ')
occurrences = int(input('Enter the number of occurrences: '))
print(split_delimiter_string(string,delimiter,occurrences))