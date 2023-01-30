#This is all about List :
list1 = ['abcd', 12345, 12.5, 'efgh', 87, 'Hello World']
list2 = [1234, 'Sadhguru']
print(list1)
print(list2)
print(list[3])#efgh
print(list1+list2)#'abcd', 12345, 12.5, 'efgh', 87, 'Hello World', 1234, 'Sadhguru'
print(list2 * 2)#1234, 'Sadhguru', 1234, 'Sadhguru'
list1[2]=56
print(list1)#'abcd', 12345, 56, 'efgh', 87, 'Hello World'
"""

In string you cannot assigen any string object
string1 = 'Hello World'
string1[6]= 'H'
print(string1)

"""
list3 = ['abcd', 12345, 12.5, ['efgh', 87, ['ijkl'], 253, 154, [45, 445]], 'Hello World']
print(list3[3][5][1])#445

#Use of append :
list3.append('PG-DAI')
print(list3)
list4 = ['Mumbai', 'Noida']
list3.append(list4)
print(list3)
del list3[3][1]#87
print(list3)
list3.remove('abcd')
print(list3)
print(len(list3))
list4 = ['abcd', 12345, 12.5, ['efgh', 87, ['ijkl'], 253, 154,154,154,154, [45, 445]], 'Hello World']
print(list4[3].count(154))
list4.insert(4 , 2009)
print(list4)
print(list2.index('Sadhguru'))
a = list4.pop(2)
print(list4)
list5 = [10 , 20 , 100, 52, 85, 54, 98, 65, 48]
list5.sort()
print(list5)
list5.reverse()
print(list5)