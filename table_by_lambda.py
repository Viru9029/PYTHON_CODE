a = [1,2,3,4,5,6,7,8,9,10]
square_list = []
for i in a:
    square_list.append(i * i)

print(square_list)
list1 = [1,2,3,4,5,6,7,8,9,10]
a = list(map(lambda x : x * 2,list1))
print(a)