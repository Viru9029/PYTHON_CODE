#9) Write a Python program to count and display vowels in text. 

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    print('Count : ', len([l for l in string if l in vowels]))
    print('Vowels : ', set([l for l in string if l in vowels]))


string = input('Enter a string : ')
count_vowels(string)