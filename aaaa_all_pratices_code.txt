#**************************************************************************
# Program to add two matrices using nested loop

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# iterate through rows
for i in range(len(X)):
    # iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)
#**************************************************************************
#add two numbers

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

sum = a + b
print(sum)
#**************************************************************************
string1 = "Hello my name is Virendra Bhagwan Kate"
#answer = string1.capitalize()#return type is str
#answer = string1.lower()#return type is str
#answer = string1.upper()#return type is str
#answer = string1.swapcase()#return type is str
#answer = string1.title()#return type is str#all word first character staring from capital letter
answer = string1.replace('Bhagwan','B.')#return type is string #replace has 3rd arguments also present they said how much time you wants to replace the new word if you are not written there so they will replace all the old word/char with new
#answer = string1.islower()#return type is boolean
#answer = string1.isupper()#return type is boolean
#str.count(countcharacter,start=0,end=lengthofstring)
#answer = string1.count('m',0)#return type is int
#answer = string1.find('m',0)#return type is int
print(answer)
print(type(answer))
#**************************************************************************
#print thr number is armstrong or not

# def armstrong(a):
#     a=a
#     temp = a
#     len_of_val = len(str(a))
#     sum = 0
#     while a != 0:
#         first = a % 10
#         sum = sum + (first**len_of_val)
#         a = a // 10
#         if temp == sum:
#             print("ArmStrong No")
#             break
#         else:
#             print('Not ArmStrong No')
#             break
#
# a = float(input("Enter the number : "))
# armstrong(a)

n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
#**************************************************************************
#Bit-wise operators
"""

2^10  2^9  2^8  2^7   2^6  2^5   2^4   2^3  2^2  2^1  2^0
  |    |    |    |     |    |    |      |    |    |    |
1024  512  256  128   64   32    16     8    4    2    1

"""
#Use of "AND(&)" operator :
"""
input1  input2   Output
1        1        1
0        0        0
1        0        0
0        1        0
"""
a = 50
b = 10
ans = a & b
print(ans)#2
print("\n")

#Use of "OR(|)" operators :
"""
input1  input2   Output
1        1        1
0        0        0
1        0        1 
0        1        1
"""
c = 54
d = 65
ans = c | d
print(ans)#119
print("\n")

#Use of "XOR(^) operators :
"""
input1  input2   Output
1        1        0
0        0        0
1        0        1 
0        1        1
"""
e = 26
f = 87
ans = e ^ f
print(ans)#77
print("\n")

#Use of <<(left shit operators) :
a = 20
ans = a << 2
print(ans)#80
print("\n")
"""
20 binaray is : 00010100
remove left side two dight ahe shift to right side then 01010000 then output is 80

"""

#Use of >> (right shit operators) :
b = 20
ans = b >> 2
print(ans)#5
"""
20 binaray is : 00010100
remove right side two dight ahe shift to left side then 00000101 then output is 5

"""

#**************************************************************************
import calendar
year = int(input("Input the year : "))
month = int(input("Input the month : "))
print(calendar.month(year, month))


#**************************************************************************
test_str1 = 'e:e:k:s:g'
test_str2 = 'g:e:e:k:s'

res = sorted(test_str1.split(':')) == sorted(test_str2.split(':'))
print(res)

#**************************************************************************
def check_sum(nums, k):
    list1 = []
    for i in range(len(nums)):
        if nums[i] == k:
            return 'true'
        for j in range(nums[i], len(nums)):
            if nums[j] == k:
                return 'true'
            elif (nums[i] + nums[j]) == k:
                list1.append(i)
                list1.append(j)
                print(list1)
                return 'true'
            else:
                return 'false'
    print(list1)


lis = [23,2, 4, 7]
k = 13
print(check_sum(lis, k))

#**************************************************************************
capial_char = ord('A')
small_char = ord('a')
capial_char_list = []
small_char_lsit = []
int_value = []
for i in range(0,26):
    cap = chr(capial_char)
    small = chr(small_char)
    capial_char_list.append(cap)
    small_char_lsit.append(small)
    int_value.append(i)
    capial_char = capial_char+1
    small_char = small_char+1

print(capial_char_list)
print(small_char_lsit)
print(int_value)



print(chr(65))
print(ord('A'))
#**************************************************************************

my_list = [1, 2, 3, 4, 5,
           6, 7, 8, 9]
start = 0
end = 12
step = 3
for i in range(start, end, step):
    x = i
    print(my_list[x:x+step])
#**************************************************************************
#area of circle
#formula = pie * r square

import math
radius = float(input("Enter the radius of circle : "))
def area_of_circle(radius):
    pi = math.pi #or 3.14
    area = pi * (radius*radius)
    print(area)

area_of_circle(radius)
#**************************************************************************
list1 = [20,50,47,85,69,75]
del list1[:]
print(list1)
print(list1.clear())

#**************************************************************************
#Consecutive characters frequency

def consective_ch_freq(word):
    count = 1
    length =""
    list1 = []
    for i in range(1,len(word)):
       if word[i-1]==word[i]:
          count+=1
       else :
           list1.append(count)
           #length = length + word[i-1]+" repeats "+str(count)+", "
           count=1
    print(list1)

str="geekksforgggeeks"
consective_ch_freq(str)

#**************************************************************************
#CONSRCUTIVE VOWELS:
#s = input().strip().lower()
s ='ASIEOPKMGETLOST'
c=0
for i in range(0,len(s)-1):
    if s[i] in 'aeiouAEIOU' and s[i+1] in 'aeiouAEIOU':
        c+=1
print(c)


s ='ASIEOPKMGETLOST'



# #s = input().strip().lower();c=0
# for i in range(len(s)-1):
#     if s[i] in 'aeiou' and s[i+1] in 'aeiou':c+=1
# print(c)
#**************************************************************************
#
# Program to print duplicates from a list of integers
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

def duplicates_in_list(list1):
    unique_in_list = list(set(list1))
    dupli_list = []
    for j in unique_in_list:
        if list1.count(j) > 1:
            dupli_list.append(j)
    print(unique_in_list)
    print(dupli_list)


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicates_in_list(list1)

#**************************************************************************
def sum_of_cube(n):
    sum = 0
    for i in range(1,int(n+1)):
        sum = sum + (i*i*i)
    print(sum)

a = float(input("Enter the any Natural Number : "))
sum_of_cube(a)
#**************************************************************************
#find Cumulative sum of a list

# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]


def cumulative_sum(list):
    cumm_sum = []
    cumm_sum.append(list[0])
    for i in range(1,len(list)):
        sum = cumm_sum[-1] + list[i]
        cumm_sum.append(sum)
    print(cumm_sum)


list1 = [10, 20, 30, 40, 50]
cumulative_sum(list1)

#**************************************************************************
"""for i in range(13):
    print(i * '+')
for j in range(13,1,-1):
    print(j * '*')"""

side = 7
height = list(range(side)) + list(reversed(range(side-1)))
#print(side,'\n', height)
pattern = '{: <{space}}{:+<{val}}'
#print(pattern)
for x in height:
    #print('x =', x)
    a = side - x - 1
    #print('a = ', a)
    b = x * 2 + 1
    #print('b = ', b)
    print(pattern.format('', '', space=a, val=b))
#**************************************************************************
# Find all duplicate characters in string
#
# Input : hello
# Output : l
#
# Input : geeksforgeeeks
# Output : e g k s

def duplicate_chr_in_string(string1):
    convert = list(string1)
    dictionary = {}
    for i in range(len(convert)):
        dictionary[convert[i]] = dictionary.get(convert[i],0)+1
    print(dictionary)
    res = [i for i in dictionary if dictionary[i] >= 2]
    print("Duplicate characters in string is : ", " ".join(res))


a = 'geeksforgeeeks'
duplicate_chr_in_string(a)
#**************************************************************************



def sum_of_list(lis,n):
    sum = 0
    index = []
    for i in range(0,len(lis)):
        for j in range(0,len(lis)):
            if (lis[i] + lis[j]) == n:
                sum += lis[i] + lis[j]
                index.append(i)
                index.append(j)
                break

    print(sum)
    print(index)


list1 = [2,3,7,11,15]
sum_of_list(list1,9)




# index2 = []
# sum1 = 0
#
# def sum_of_list1(lis,n):
#     lis.sort()
#     index2 = []
#     for i in range(0,len(lis)):
#         if lis[i] <= n:
#             index2.append(i)
#     for i in range(0,len(lis)):
#
#
#
#
#
#
# list1 = [2,3,7,11,15]
# sum_of_list(list1,9)
#
#
# result = filter(lambda x : if x is <=9,list1)
# print(result)
#**************************************************************************
#Check if element exists in list or not


def element_exit(list,n):
    if n in list:
        print('exist')
    else:
        print('not exist')


list1 = [10,20,4,0,50,78,60,3,5,8,9,85,76,69,28,69,28,5]
element_exit(list1,95)
#**************************************************************************
# all even no in given range

def even_no_in_range(x,y):
    even_no = []
    for i in range(x,y):
        if i % 2 == 0:
            even_no.append(i)
    print(even_no)

even_no_in_range(4,15)
#**************************************************************************
#even no in the list


def even_no(list):
    even_no_list = []
    for i in list:
        if i % 2 ==0:
            even_no_list.append(i)
        else:
            continue
    print(even_no_list)

list = [2,0, 7, 5, 64, 14]
even_no(list)


#**************************************************************************
#Python program to print even length words in a string

# Input: s = "This is a python language"
# Output: This is python language

def even_word_print(string):
    split_word = string.split(" ")
    list1 = []
    for i in range(len(split_word)):
        if i % 2 == 0:
            print(split_word[i])
            #list1.append(split_word[i])
    print(list1)

s = "This is a python language"
even_word_print(s)

#**************************************************************************
#factorial code

a = float(input("Enter the number : "))

def factorial(n):
    return 1 if (n == 0 or n ==1) else n * factorial(n - 1)

print(factorial(a))
#**************************************************************************
# Function for nth Fibonacci number

def fibonacci(n):
    if n <= 0:
        print("Invalid Number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))
#**************************************************************************
#to interchange first and last elements in a list


list1 = [12, 35, 9, 56, 24]

def change_fist_last_ele(list1):
    first = list1[:1]
    last = list1[-1:]
    list1[:] = last + list1[1:len(list1)-1] + first
    print(list1)

change_fist_last_ele(list1)



#**************************************************************************
#Identity Operators
#use of "is" and "is not" operater with integer number
d = 5
f = 5
print(d is f)#True
print(d is not f)#False

#Use of "is" and "is not" operator with string
a = 'Sadhguru'
b = 'Sadhguru'
print(a is b)#True
print(a is not b)#False

#Use of "is" and "is not" operator with List bit in list its work opposite
#when list is True then they return False and If List is False they return True
c = [1, 4, 7]
e = [1, 4, 7]
print(c is e)#False
print(c is not e)#True
#**************************************************************************


l1=[]
l2=[]
l3=[]
final=[]
char1_start=ord('A')
char_start=ord('a')
a=input("enter your name or string:")
for i in range(1,27):
    p=chr(char_start)
    k=chr(char1_start)
    l1.append(p)
    l2.append(i)
    l3.append(k)
    char1_start=char1_start+1
    char_start=char_start+1

a = a.lower()
split_output = a.split()
print(split_output)

for i in range(len(split_output)):
    sum = 0
    for j in range(len(split_output[i])):
        present = split_output[i]
        for k in range(len(l1)):
            if present[j] == l1[k]:
                sum = sum + l2[k]
    final.append(sum)
               
# #sorted_array = np.sort(final)
# print("this is final answer:",#sorted_array)
#**************************************************************************
values = []
keys = []
a = ord('a')
for i in range(1,27):
    b = chr(a)
    keys.append(b)
    values.append(i)
    a += 1

print(keys)
print(values)

dictionary = dict(zip(keys,values))
print(dictionary)


def sum_of_words(str):
    split_word = str.split()
    sum = []
    for i in range(len(split_word)):
        count = 0
        present_word = split_word[i]
        for j in range(0,len(present_word[i])):
            print(len(present_word[i]))
            print(present_word[j])
            if present_word[j] in dictionary:
                count += dictionary.get(present_word[j])
            sum.append(count)
    print(sum)

stringss = 'i am boss'
sum_of_words(stringss)
#**************************************************************************
#find length of list


def leng_list(list):
    counter = 0
    for i in list:
        counter += 1
    print(counter)


list1 = [10,20,1,0,1,2,6,9,8,5,3,8,2,6,98,8,2,6,8,7,5]
leng_list(list1)


print(len(list1))
#**************************************************************************

def fine_location_of_word_in_string(st,word):
    split_word = st.split()
    index_no = ""
    for i in range(len(split_word)):
        if split_word[i] == word:
            index_no += str(i+1)
    print(index_no)
    print(type(index_no))




str1 = 'geeksforgeeks is best for geeks'
find_word = 'best'
fine_location_of_word_in_string(str1,find_word)
#**************************************************************************
#Logical Operators
#Use of "and" operator : if both the operend are true then it will True other wise False
print(True and True)#True
print(False and False)#False
print(True and False)#False
print(False and True)#False
print("\n")

#Use of "or" operator : if both the operend are true and if any one operend are true then it will return True
#and if both the operend are false then it will take False
print(True or True)#True
print(False or False)#False
print(True or False)#True
print(False or True)#True
print("\n")

#Use of "not" operator : if the operator are True it will return false and
#if the operator are False the it will return True
print(not True)#false
print(not False)#True
#**************************************************************************
test_str = "GeeksfoorrGeeks"

def max_freq_char(string):
    tuple1 = tuple(string)
    list1 = []
    for i in tuple1:
        list1.append(0)
    dictinary = dict(zip(tuple1,list1))
    for j in range(len(tuple1)):
        if tuple1[j] in dictinary.keys():
            dictinary[tuple1[j]] += 1
    print(dictinary)
    res = max(dictinary.values())
    a = [k for k in dictinary if dictinary[k] == res]
    print(a)
    list3 = []
    list4 = []
    for key,value in dictinary.items():
        list3.append(key)
        list4.append(value)
    for i in range(len(list4)):
        if list4[i] == res:
            print("This is least no repeted word : ",list3[i])
        else:
            continue


max_freq_char(test_str)

# all_freq = {}
# for i in test_str:
#  if i in all_freq:
#   all_freq[i] += 1
#  else:
#   all_freq[i] = 1
# res = max(all_freq, key = all_freq.get)
#**************************************************************************
#max array

def max_element_array(a):
    for i in a:
        return max(a)

l = [15,6,8,9,8,62,72,92,522,5,262,2,22,25,0,2,2,6,59,56,59,5]
print(max_element_array(l))



#**************************************************************************
#print maximum no in two between two variable


a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

def maximum(a,b):
    if a >= b:
        print(a)
    else:
        print(b)

maximum(a,b)


max_no = max(a,b)
print('maximum no : ',max_no)
#**************************************************************************
#Membership operator
#Use of "in" operator : with the help of string
x = 'Hello World'
print('Hello' in x)#True
print('H' in x)#True
print('hello' in x)#false because python is case-sensitive language
print("\n")

#Use of "in" operator : with the help of dictonary
#in dictonary you have to use only key ex{1: } this is key
# not value ex{ :'a'} this is value
y = {1:'a', 2:'b', 3:'c'}#dictonary
print(1 in y)#True
print('b' in y)#False
print("\n")

#Use of "not in " operator : with the help of string
z = 'Hello World'
print('Hello' not in z)#false because Hello is present
print('H' not in z)#false because H is present
print('hello' not in z)#True because hello is not present
print("\n")

#Use of "not in" operator : with the help of dictonary
#in dictonary you have to use only key ex{1: } this is key
# not value ex{ :'a'} this is value
y = {1:'a', 2:'b', 3:'c'}#dictonary
print(1 not in y)#False because 1 is present it will return false
print('b' not in y)#True because 'b' is not present as a key so it will returnm true
print("\n")


#**************************************************************************
#Least Frequent Character in String

test_str = "GeeksfoorrGeeks"

def least_freq_char(string):
    tuple1 = tuple(string)
    list1 = []
    for i in tuple1:
        list1.append(0)
    dictinary = dict(zip(tuple1,list1))
    for j in range(len(tuple1)):
        if tuple1[j] in dictinary.keys():
            dictinary[tuple1[j]] += 1
    print(dictinary)
    res = min(dictinary.values())
    list3 = []
    list4 = []
    for key,value in dictinary.items():
        list3.append(key)
        list4.append(value)
    for i in range(len(list4)):
        if list4[i] == res:
            print("This is least no repeted word : ",list3[i])
        else:
            continue


least_freq_char(test_str)
#**************************************************************************
#min max code

def maximumChars(str):
    n = len(str)
    res = -1
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (str[i] == str[j]):
                res = max(res, abs(j - i - 1))
                print(res)
    return res

print(maximumChars('aabaaaaaaaaaaaaaabaaab'))




def minmax(str):
    seperate_word = list(str)
    lista = []
    lisrb = []
    for i in range(0,len(seperate_word)):
        if seperate_word[i] == 'a':
            lista.append(i)
        else:
            lisrb.append(i)
    x = (lista[-1] - lista[0])
    y = (lisrb[-1] - lisrb[-2])
    result = x + y
    return result

print(minmax('aabaaaaaaaaaaaaaabaaab'))

# a="aabaaaaaaaaaaaaaabaaab"
# c=[]
# d=[]
# bb=[]
# l1=[]
#
# for i in range(0,len(a)):
#     c.append(a[i])
#     if a[0]==a[i]:
#         c.append(i)
#     if a[0]!=a[i]:
#         bb.append(i)
#
# x=bb[-1]-bb[-2]
# for i in range(0,len(bb)):
#    final= bb[-1]-bb[-i]
#    l1.append(final)
# l1.sort()
# y=l1[1]
# print(x+y)
#**************************************************************************
def adding(x,y):
    return x+y

def subtracting(x,y):
    return x-y

def multiplying(x,y):
    return x*y

def dividing(x,y):
    return x/y

#**************************************************************************
class X :
    pass
class Y :
    pass
class Z :
    pass

class A(X,Y):
    pass
class B(Y,Z):
    pass
class M(B,A,Z):
    pass
print(M.mro())

#**************************************************************************
#multiplication of all the element in the list


def multi_all_element(list):
    sum = 1
    for i in list:
        sum = sum * i
    print(sum)

list1 = [1,2,3]
multi_all_element(list1)
#**************************************************************************
#negative no in list


def negative_no_in_list(list):
    negative_list = []
    for i in list:
        if i < 0:
            negative_list.append(i)
        else:
            continue
    print(negative_list)

list1 = [12, -7, 5, 64, -14]
negative_no_in_list(list1)



neg_nos = list(filter(lambda x: (x < 0), list1))
print(neg_nos)
#**************************************************************************
# Count the Number of matching characters in a pair of string
#
# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4
# (i.e. matching characters :- a, d, e, f)
#
# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5
# (i.e. matching characters :- b, 1, 2, @, k)

def count_no_of_matching_char_in_string(string1,string2):
    list1 = set(list(string1))
    list2 = set(list(string2))
    matching = list1 & list2
    print(len(matching))


str1 = 'abcdef'
str2 = 'defghia'
count_no_of_matching_char_in_string(str1,str2)

def count_no_of_matching_char_in_string2(string1,string2):
    list1 = list(string1)
    list2 = list(string2)
    find_word = []
    for i in list1:
        if i in list2:
            find_word.append(i)
    for j in list2:
        if j in list1:
            find_word.append(j)
    result = set(find_word)
    print(len(result))

str1 = 'abcdef'
str2 = 'defghia'
count_no_of_matching_char_in_string2(str1,str2)
#**************************************************************************
#n largest no in list


def nth_largest_no(list,nth_no):
    list.sort()
    print(list)
    largest_no = list[-nth_no:]
    print(largest_no)


l1 = [10,25,6,9,8,89,56,87,5,4,7,58,26,9,8,68,698,2,6,8,3,59,3,59,3,3,8,6,32,58,25,8,2,8,7,88,2,9,2,5,20,5]
nth_largest_no(l1,5)
#**************************************************************************
# Python program to find the character position of Kth word from a list of strings
# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
# Output : 0
# Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 15
# Output : 1
# Explanation : 15th index occurs in “best” and point to “e” which is 1st element of word.

def find_position_of_character(lis, nth):
    list1 = []
    for i in range(0, len(lis)):
        for j in range(0, len(lis[i])):
            list1.append(str(j))
    print(list1)
    if list1[nth]:
        print(list1[nth])
    else:
        print('Index out of range')


test_list = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
K = 21
find_position_of_character(test_list, K)

#**************************************************************************
#Count occurrences of an element in a list

#Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
#Output: 3


def occ_element(list,x):
    count = 0
    for i in range(len(list)):
        if x == list[i]:
            count += 1
    print(count)

list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
occ_element(list1,10)
#**************************************************************************
#print odd no in list


def odd_no_in_list(list):
    odd_no = []
    for i in list:
        if i % 2 == 0:
            continue
        else:
            odd_no.append(i)
    print(odd_no)
    print(" ".join(odd_no))


list1 = [2, 7, 5, 64, 14]
odd_no_in_list(list1)
#**************************************************************************
# odd no in given range


def odd_no_in_range(x,y):
    odd_no_list = []
    for i in range(x,y+1):
        if i % 2 != 0:
            odd_no_list.append(i)
    print(odd_no_list)

odd_no_in_range(4,15)
#**************************************************************************
def palindrome_search(s):
    m = ''  # Memory to remember a palindrome
    for i in range(len(s)):  # i = start, O = n
        for j in range(len(s), i, -1):  # j = end, O = n^2
            if len(m) >= j-i:  # To reduce time
                break
            elif s[i:j] == s[i:j][::-1]:
                m = s[i:j]
                break
    return m


print(palindrome_search('babad'))

#**************************************************************************
#string is palindrome or not

a = 'malayalam'


if a == a[::-1]:
    print(a)
#**************************************************************************
# positive no in given list

def positive_no(list):
    positive_no_list = []
    for i in list:
        if i > 0:
            positive_no_list.append(i)
        else:
            continue
    print(positive_no_list)


list1 = [12, -7, 5, 64, -14]
positive_no(list1)

#**************************************************************************
#prime no

def prime_no(x,y):
    prime_list = []
    for i in range(x,y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    print(prime_list)

prime_no(0,101)



#check wheter prime no or not
def check_prime_no(a):
    if a == 0 or a == 1:
        print("NOT PRIME no")
    else:
        for i in range(2,int(a/2)+1):
            if a % i == 0:
                print("No is NOT PRIME")
                break
        else:
            print("Number is PRIME")

check_prime_no(9)


#**************************************************************************
# Remove after substring in String


def remove_string_after_substring(str, substring):
    split_string = str.split()
    for i in range(len(split_string)):
        if split_string[i] == substring:
            res = split_string[:i] + [substring]
            print(" ".join(res))


test_str = 'geeksforgeeks is best for geeks'
sub_str = "best"
remove_string_after_substring(test_str, sub_str)

#**************************************************************************
import numpy as np

a = np.arange(15).reshape(3,5)
print(a)
#**************************************************************************
import random
a = random.randint(0,100)
print(a)
#**************************************************************************
import functools
lis = [1, 3, 5, 500, 1200, 2]
print(functools.reduce(lambda a, b: a if a + b == 4 else b, lis))
#**************************************************************************
from functools import reduce
arr = [100, 10, 5, 25, 35, 14]
sum_1 = reduce(lambda x, y: x*y, arr)
print(sum_1)

print(sum_1 % 11)
#**************************************************************************
# Remove all duplicates from a given string in Python
#
# Input : geeksforgeeks
# Output : efgkors


def duplicate_in_string(string):
    list1 = set(string)
    print(''.join(list1))

Input = 'geeksforgeeks'
duplicate_in_string(Input)
#**************************************************************************
#remove element from the list take any condition


def remove_ele(list):
    remove_elemet = []
    for i in list:
        if i % 2 ==0:
            remove_elemet.append(i)
            list.remove(i)
    print("After removing condition no in list : " ,list)
    print('Removing element in list : ', remove_elemet)



list1 = [12, 15, 3, 10]
remove_ele(list1)
#**************************************************************************
# remove empty list from list

def remove_empty_list(list):
    element = []
    for i in list:
        if i:
            element.append(i)
    print(element)

input_list = [5, 6, [], 3, [], [], 9]
remove_empty_list(input_list)
#**************************************************************************
# Python program for removing i-th character from a string
#
# g
# e
# e
# k
# s
# 0
# 1
# 2
# 3
# 4
# Examples:
#
# Input: Geek
# i = 1
# Output: Gek
#
# Input: Peter
# i = 4
# Output: Pete

def remove_ith_no_chr_from_string(strings,i):
    if i <= (len(strings)):
        first = strings[:i]
        second = strings[i+1:]
        final = first + second
        print(final)
    else:
        print("Enter the valid index")


stri = 'Geek'
remove_ith_no_chr_from_string(stri,3)
#**************************************************************************
#Remove the ith character from the string using the native method

def remove_chr(a,n):
    print(len(a))
    string = a.replace(n,'',1)
    print(string)


remove_chr("GeeksForGeeks",'s')

def remove_chr_by_index_no(a,n):
    while n <= len(a)-1:
        first = a[:n]
        second = a[n+1:]
        final = first + second
        print(final)
        break
    else:
        print('Please enter valid index no')

remove_chr_by_index_no("GeeksForGeeks",0)
#**************************************************************************
import string
print(string.punctuation)


def remove_punch(str):
    punch = string.punctuation
    for ele in str:
        if ele in punch:
            str = str.replace(ele,'')
    print(str)


test_str = "Gfg, is best : for ! Geeks ;"
remove_punch(test_str)

#**************************************************************************
# remove empty tuple form list

def remove_tuple(list):
    list_without_tuple = []
    for i in list:
        if i:
            list_without_tuple.append(i)
    print(list_without_tuple)


list1 = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
remove_tuple(list1)

#**************************************************************************
for number in range(0,12):
    if number  > 1:
        for i in range(2,number):
            if (number%i)==0:
             break
        else:
            print(number)
#**************************************************************************
#Python – Ways to remove multiple empty spaces from string List
# The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
# List after filtering non-empty strings : ['gfg', 'is', 'best']


test_str = ['gfg', '   ', ' ', 'is', '            ', 'best']

def remove_empty_spaces(str):
    adter_list = []
    for i in str:
        if i.strip():
            adter_list.append(i)
    print(adter_list)

remove_empty_spaces(test_str)


#**********second way**********************

a = [ele for ele in test_str if ele.strip()]
print(a)
#**************************************************************************
#     original string is : geeksforgeeks is best
# The String after performing replace: ge*k*fo*ge*ks is best
from os import replace


test_list = [2, 4, 7, 10]
test_str = 'geeksforgeeks is best'
repl_char = '*'


def replace_specific_index_no(str, sep_list, replace_item):
    a = list(test_str)
    for i in sep_list:
        a[i] = replace_item
    print(''.join(a))


replace_specific_index_no(test_str, test_list, repl_char)

#************Second Way *******************************
convert_list = list(test_str)
a = [repl_char if index in test_list else ele for index, ele in enumerate(convert_list)]
print(''.join(a))

#**************************************************************************
# Replace all occurrences of a substring in a string
#
# Input : test_str = “geeksforgeeks” s1 = “geeks” s2 = “abcd”
#
# Output : test_str = “abcdforabcd” Explanation : We replace all occurrences of s1 with s2 in test_str.
#
# Input : test_str = “geeksforgeeks” s1 = “for” s2 = “abcd”


def replace_substring(string,string_word,replace_word):
    find_word_in_string = string.split(string_word)
    print(find_word_in_string)
    str = ""
    for i in find_word_in_string:
        if i == '':
            str += replace_word
        else:
            str += i

    print(str)


test_str = 'geeksforgeeks'
s1 = 'geeks'
s2 = 'abcd'
replace_substring(test_str,s1,s2)
#**************************************************************************
# word_list = ["best", 'CS', 'for']

# # initializing replace word
# repl_wrd = 'gfg'


def replace_word(str, word_list, replace_wd):
    dictonary = {}
    new_str = []
    for i in word_list:
        dictonary[i] = replace_wd
    for j in str.split():
        if j in dictonary:
            new_str.append(dictonary.get(j))
        else:
            new_str.append(j)
    print(dictonary)
    print(" ".join(new_str))


word_list = ["best", 'CS', 'for']
repl_wrd = 'gfg'
test_str = 'Geeksforgeeks is best for geeks and CS'
replace_word(test_str, word_list, repl_wrd)

#**************************************************************************
#Replace duplicate Occurrence in String


# initializing string
test_str = 'Gfg is best . Gfg also has Classes now . Classes help understand better'


repl_dict = {'Gfg' : 'It', 'Classes' : 'They' }

def replace_word_in_exiting_words(string):
    convert_into_words = string.split()
    for i in range(len(convert_into_words)):
        if convert_into_words[i] in repl_dict:
            convert_into_words[i] = repl_dict.get(convert_into_words[i])
    print(convert_into_words)
    print(" ".join(convert_into_words))

replace_word_in_exiting_words(test_str)
#**************************************************************************
str = "helloello0"


def revese_midd(stringsss):
    first = stringsss[:int(len(stringsss) / 2)]
    mid = stringsss[int(len(stringsss) / 2):int(len(stringsss) / 2) + 1]
    last = stringsss[int(len(stringsss) / 2) + 1:]
    output = first[::-1] ," " + mid , " " + last[::-1]
    print(output)


revese_midd(str)

#**************************************************************************
def signal_light(str,k):
    dist1 = {'R':'G','B':'R','G':'B'}
    dist2 = {'R':'B','B':'G','G':'R'}
    final = ""
    if k == 1:
        for i in range(len(str)):
            if str[i] in dist1:
                final += dist1.get(str[i])
    elif k == 2:
        for i in range(len(str)):
            if str[i] in dist2:
                final += dist2.get(str[i])
    return final

print(signal_light('RBRG',1))
#**************************************************************************
#simple interest program

principle_amount = float(input("Enter Principal Amount : "))
time = float(input("Enter the time period : "))
rate_of_int = float(input("Enter the rate of interest : "))

def simple_interest(p,t,r):
    simple_int = (p*t*r)/100
    print(simple_int)
    return simple_int

simple_interest(principle_amount,time,rate_of_int)
#**************************************************************************
#smallest largest second smallest second largest no find in the list


def small_largest_elemt(list):
    list.sort()
    print(list)
    smallest_element = list[0]
    second_smallest_element = list[1]
    largest_element = list[-1]
    second_largest_element = list[-2]
    print(smallest_element," ",second_smallest_element," ",largest_element," ",second_largest_element)

l1 = [10,20,30,5,97,39,42,99,75,6,9,2,99,33,89,63,58,99,3598,6,9,63,8,9,63,5,96,3,9,5,36,9,23,9,93,6]
small_largest_elemt(l1)
#**************************************************************************
# Sort String list by K character frequency
# Input : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”], K = ‘s’ 
# Output : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’] 
# Explanation : bessst has 3 occurrence, geeksforgeekss has 3, and so on.

# Input : test_list = [“geekforgeekss”, “is”, “bessst”], K = ‘e’ 
# Output : [“geekforgeekss”, “bessst”, “is”] 
# Explanation : Ordered decreasing order of ‘e’ count. 


def sort_asc_list(list1):
    list1.sort()
    print(list1)
    
    
lis = ['geekforgeekss', 'is', 'bessst', 'for', 'geeks']
K = 's'   
sort_asc_list(lis)
#**************************************************************************
#Sort the values of first list using second list in Python

def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [x for _, x in sorted(zipped_pairs)]
    return z


# driver code
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))
#**************************************************************************
import re


def spliting_string_from_vowels(str):
    a = re.split('a|e|i|o|u', str)
    print(a)


test_str = 'GFGaBste4oCS'
spliting_string_from_vowels(test_str)

#**************************************************************************
#Python program to split and join a string

# Split the string into list of strings
#
# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']
#
#
# Join the list of strings into a string based on delimiter ('-')
#
# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks

def split_join_string(string):
    spliting = string.split()
    print(spliting)
    joining = "_".join(spliting)
    print(joining)



stri = 'Geeks for Geeks'
split_join_string(stri)
#**************************************************************************
#find square root of complex number.
import cmath

# num = 1+2j
num = eval(input("Enter the value : "))

sq = cmath.sqrt(num)
print(sq)
#**************************************************************************
#find square root

a = float(input("Enter the value : "))
sq_root = a ** 0.5
print(sq_root)


import numpy as np
sq_root1 = np.sqrt(a)
print(sq_root1)
#**************************************************************************
#Check if a given string is binary string or not

# Input: str = "01010101010"
# Output: Yes
#
# Input: str = "geeks101"
# Output: No

def string_binary_or_not(strings):
    unique_words_in_string = list(set(strings))
    print(unique_words_in_string)
    if unique_words_in_string == (['0','1'] or ['1','0']):
        print("String is Binary")
    else:
        print("String is NOT Binary")


str = "geeks101"
string_binary_or_not(str)
#**************************************************************************
#Program to check if a string contains any special character


import re
def special_chr_yes_or_not(string):
    reg = re.compile('[@_!#$%^&*()<>}{":|?/]')
    if (reg.search(string)) == None:
        print("String is accepted")
    else:
        print("String is not accepted")

strings = 'Geeks For Geeks'
special_chr_yes_or_not(strings)
#**************************************************************************
#String slicing in Python to check if a string can become empty by recursive deletion

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.


# Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
# Output : No
# Explanation : In the string it is not possible to make the
#               string empty in any possible manner.

def from_string_remove_substring(str,substring):
    index1 = str1.split('GEEKS')
    rem_str = "".join(index1)
    res = ['True' if rem_str == substring else 'False']
    print("".join(res))
    
str1 = "GEEGEEKSSGEK"
sub = 'GEEKS'
from_string_remove_substring(str1,sub)
#**************************************************************************
def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
#******************************
txt = "Hello World"[::-1]
print(txt)
#**********************************
a = 'hello bro'
print(a[::-1])
#***********************************
def reverse(str):
    str = str[::-1]
    return str
#*******************************
s = 'hello world'
print(reverse(s))
#*****************************
b = ""
for i in s[::-1]:
    b = b + i
print(b)
#********************************
b = []
for i in s[::-1]:
    b.append(i)
print(b)
#*****************************************
s = "i like this program very much"
output = 'much very program this like i'

words = s.split()
print(words)
strings = []
for i in words[::-1]:
    strings.append(i)
print(strings)
print(" ".join(strings))
#******************************************
str1 = "Analytics Vidhya"

list_split = str1.split()
print(list_split)

a = list(str1)
print(a)
#**************************************************************************
#String slicing in Python to rotate a string

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee"

def string_slicing(str,d):
    left_rotation = str[d:] + str[:d]
    right_rotation = str[len(str)-d:] + str[:len(str)-d]
    print(left_rotation)
    print(right_rotation)
    
s = "qwertyu"
d = 2
string_slicing(s,d)
#**************************************************************************
# Successive Characters Frequency
# Input : test_str = ‘geeks are for geeksforgeeks’, que_word = “geek” Output : {‘s’: 3} 
# Input : test_str = ‘geek’, que_word = “geek” Output : {}
import re
def repeted_substring_count(str,substring):
    index = re.findall(substring,str)
    count = 0
    for i in range(len(index)):
        if index[i] == substring:
            count += 1
    print(substring, ' : ',count)
    
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'
que_word = 'geek'
repeted_substring_count(test_str,que_word)
#**************************************************************************
#Check if a Substring is Present in a Given String

# Example 1: Input : Substring = "geeks"
#            String="geeks for geeks"
# Output : yes

def string_present(string1,substring):
    if substring in string1:
        print('present substring')
    else:
        print('not present')

string_present("geeks for geeks","geeks")
#**************************************************************************
#find sum of array


def sum_of_array(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)

list1 = [1,2,3,4,5,6,7,8,9,10]
sum_of_array(list1)
#**************************************************************************
l1=[]
l2=[]
l3=[]
final=[]
le_n=[]


char_start=ord('a')
a=input("enter your name or string:")
a=a.lower()
for i in range(1,27):
    p=chr(char_start)
   
    l1.append(p)
    l2.append(i)
 
    
    char_start=char_start+1
b=a.split()
for i in range(0,len(b)):
    result=[]
    for j in range(0,len(b[i])):
        
        
        for k in range(0,26):
            if b[i][j]==l1[k]:
                result.append(l2[k])
    final.extend([result])
for i in final:
    b=sum(i)
    le_n.append(b)
print(sorted(le_n))
#**************************************************************************
#sum of element in the list


def sum_of_element(list):
    sum = 0
    for i in list:
        sum += i

    print(sum)


list1 = [10,20]
sum_of_element(list1)
#**************************************************************************
#Sum of squares of first n natural numbers

def sum_square(n):
    sum = 0
    for i in range(1,int(n)+1):
        sum = sum+(i*i)
    print(sum)

a = float(input("Enter the natural number : "))
sum_square(a)
#**************************************************************************


def swap_list(list):
    temp = list[0]
    list[0]=list[2]
    list[2]=temp
    print(list)

List1 = [23, 65, 19, 90]
print(swap_list(List1))
#**************************************************************************
#swap case
a = 5
b = 10

temp = a
a = b
b = temp
print('a =',a, 'b =',b)



c = 15
d = 20

c , d = d,c
print(c,d)
#**************************************************************************
# Python program to check whether the string is Symmetrical or Palindrome
#
# Input: khokho
# Output:
# The entered string is symmetrical
# The entered string is not palindrome
#
# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome


def symmetrical(a):
    n = len(a)
    if n % 2==0:
        mid = (n // 2)+1
        print(mid)
    else:
        mid = n // 2
        print(mid)

    while True:
        if a[:mid-1] == a[mid-1:]:
            print("string is symmetric")
            break
        else:
            print('string not symmetric')
            break

b='amaama'
symmetrical(b)
#**************************************************************************
a = [1,2,3,4,5,6,7,8,9,10]
square_list = []
for i in a:
    square_list.append(i * i)

print(square_list)
list1 = [1,2,3,4,5,6,7,8,9,10]
a = list(map(lambda x : x * 2,list1))
print(a)
#**************************************************************************

numbers = {1: 1, 2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
           7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z'], '*': '*', 0: 0, '#': '#'}

def for_single_enter_no(num):
    print(numbers.get(num))

def for_two_enter_no(num):
    covert = list(str(num))
    combination_list = []
    first_no = int(covert[0])
    second_no = int(covert[1])
    first_no_letter = numbers[first_no]
    second_no_letter = numbers[second_no]
    for i in range(len(numbers[first_no])):
        for k in range(len(numbers[first_no])):
            combination_list.append(first_no_letter[i] + second_no_letter[k])
    print(combination_list)

def letter_combination_of_number(no):
    if len(no) == 1:
        no1 = int(no)
        for_single_enter_no(no1)
    elif len(no) == 2:
        no1 = int(no)
        for_two_enter_no(no1)
    else:
        print('Other combination in progress')


n1 = 1
letter_combination_of_number('97')

#**************************************************************************
# The original string is : geeksforgeeks_is_best
# The String after changing case : GeeksforgeeksIsBest

def string_title(str):
    str2 = str.replace("_"," ").title().replace(" ","")
    print(str1)
    
str1 = 'geeksforgeeks_is_best'    
string_title(str1)
#**************************************************************************
#calculate area of triangle
a = float(input())
b = float(input())
c = float(input())

#semiperimetr
semi = (a+b+c)/2

area_of_triangle = (semi * (semi-a) * (semi-b) * (semi-c)) ** 0.5

print(area_of_triangle)
#**************************************************************************
# Python program to find uncommon words from two Strings
#
# Input : A = "Geeks for Geeks"
#         B = "Learning from Geeks for Geeks"
# Output : ['Learning', 'from']
#
# Input : A = "apple banana mango"
#         B = "banana fruits mango"
# Output : ['apple', 'fruits']

def uncommon_words_in_string(string1,string2):
    dictionay = {}
    for word1 in string1.split():
        dictionay[word1] = dictionay.get(word1,0) + 1

    for word2 in string2.split():
        dictionay[word2] = dictionay.get(word2,0) +1

    print(dictionay)
    res = [i for i in dictionay if dictionay[i] == 1]
    print(res)


A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
uncommon_words_in_string(A,B)
#**************************************************************************
#Program to accept the strings which contains all vowels.

# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present
#
# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present


def string_contain_all_vowels_or_not(string):
    word_separate = list(string)
    vowles = ['a','e','i','o','u','A','E','I','O','U']
    present_vowles = []
    for i in range(len(word_separate)):
        if word_separate[i] in vowles:
            present_vowles.append(word_separate[i].lower())

    unique_vowles = list(set(present_vowles))
    unique_vowles.sort()
    print("Find vowels in string is : ",unique_vowles)
    vowles_lower = ['a','e','i','o','u']
    if unique_vowles == vowles_lower:
        print("Accepted")
    else:
        print("Not Accepted")


list2 = 'geeksforgeeks'
string_contain_all_vowels_or_not(list2)


#**************************************************************************
# Words Frequency in String Shorthands

# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}

# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

def count_word_in_string(str):
    split_word = str.split()
    unique_words = set(split_word)
    dictionary = {}
    for i in range(len(split_word)):
        if split_word[i] in dictionary:
            dictionary[split_word[i]] = dictionary.get(split_word[i],0)+1
        else:
            dictionary[split_word[i]] = dictionary.get(split_word[i],0)+1
    print(dictionary)


test_str = 'Gfg Gfg Gfg'
count_word_in_string(test_str)
#**************************************************************************
#Words Frequency in String Shorthands

# Input : test_str = ‘Gfg is best’
# Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
#
# Input : test_str = ‘Gfg Gfg Gfg’
# Output : {‘Gfg’: 3}

def word_freq_count(sentence):
    split_sentence = sentence.split()
    unique_words_in_sentense = list(set(split_sentence))

    count = []
    for i in range(len(unique_words_in_sentense)):
        count.append(0)

    dictionary = dict(zip(unique_words_in_sentense,count))

    for i in range(len(split_sentence)):
        if split_sentence[i] in dictionary.keys():
            dictionary[split_sentence[i]] += 1
        else:
            continue
    print(dictionary)

test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'
word_freq_count(test_str)
#**************************************************************************
# Find words which are greater than given length k
#
# Input : str = "hello geeks for geeks
#           is computer science portal"
#         k = 4
# Output : hello geeks geeks computer
#          science portal
# Explanation : The output is list of all
# words that are of length more than k.
#
# Input : str = "string is fun in python"
#         k = 3
# Output : string python

def greater_len_word_accepted(strings,len_word_accepted):
    list2 = strings.split()
    res = []
    for i in range(len(list2)):
        if len(list2[i]) > len_word_accepted:
            print(list2[i], end=" ")
            #res.append(list2[i])


str1 = "hello geeks for geeks is computer science portal"
greater_len_word_accepted(str1,5)


#**************************************************************************
list1 = ['a','c','e','g']
list2 = ['b','d','f','h']

conlist = [x+y for x,y in zip(list1,list2)]
print(conlist)
#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************

#**************************************************************************