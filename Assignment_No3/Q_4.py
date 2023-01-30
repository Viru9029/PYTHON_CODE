#4.	Write a program to accept 10 different strings and convert it into tuple and print it.
def diff_string_convert_to_tuple(strings):
    a = tuple(i for i in strings)
    print(a)

strings = [input('Enter the %d string : ' %(i)) for i in range(1,11)]
diff_string_convert_to_tuple(strings)