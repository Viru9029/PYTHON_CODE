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

