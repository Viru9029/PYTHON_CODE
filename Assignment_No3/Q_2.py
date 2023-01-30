#2.	Write a program to accept 10 different strings and convert it into list and print it.
def diff_string_convert_to_list(strings):
    print(strings)
    


strings = [input('Enter the {0} no String :'.format(i)) for i in range(1,11)]
#strings = input("Note : Enter comma , to seperate the string.\nEnter the String : ").split(',')[:10]
#strings = input('Enter the string : ').split(',')[:10]
diff_string_convert_to_list(strings)