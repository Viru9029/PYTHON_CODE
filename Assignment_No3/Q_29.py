# 29.	 Write a Python program to create a Caesar encryption 
# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
# aesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed 
# number of positions down the alphabet. For example, with a left shift of 3, D would be 
# replaced by A, E would become B, and so on. The method is named after Julius Caesar, 
# who used it in his private correspondence.
def caesar_encry(string,s):
    lower_case = [chr(i) for i in range(65,91)]
    lower_case2 = [i for i in lower_case[s:]+lower_case[:s]]
    upper_case= [chr(i) for i in range(97,123)]
    upper_case2 = [i for i in upper_case[s:]+upper_case[:s]]
    dict = {}
    for i in range(len(lower_case)):
        dict[lower_case[i]]=lower_case2[i]
        dict[upper_case[i]]=upper_case2[i]
    for i in string:
        if dict[i] in dict.keys():
            print(dict[i],end="")

        


string = input('Enter the string : ')
shift_val = int(input('Enter shift no : '))
caesar_encry(string,shift_val)
# print(chr(65))#A
# print(chr(90))#Z
# print(chr(97))#a
# print(chr(122))#z




















































































