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