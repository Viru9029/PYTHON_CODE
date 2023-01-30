lis = [1,2,3,4,5]
lis2 = [6,7,8,9,10]
lis3 = [11,12,13,14,15]

comb = [i+j+k for i,j,k in zip(lis,lis2,lis3)]
print(comb)