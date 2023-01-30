list1 = ['a','c','e','g']
list2 = ['b','d','f','h']

conlist = [x+y for x,y in zip(list1,list2)]
print(conlist)