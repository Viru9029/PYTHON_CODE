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