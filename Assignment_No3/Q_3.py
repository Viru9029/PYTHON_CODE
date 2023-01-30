#3.	Write a program to accept 10 different strings and convert it into dictionary and print it.
def diff_string_convert_to_dict(strings):
    a={i:strings[i] for i in range(len(strings))}
    print(a)
    

#strings=input('Note:Enter the comma , seperated strings. \nEnter the Strings').split(',')[:10]
strings = [input('Enter the %d string : '%(i)) for i in range(1,11)]
diff_string_convert_to_dict(strings)