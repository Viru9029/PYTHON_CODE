import array as arr
a = arr.array('i', [1, 2, 3])
print(a)


a.append(15)


for i in range(0, 4):
    print(a[i])
