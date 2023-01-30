a = ['a','b','c']
b = [1,2,3,65,84,93]
result = {}
for i,j in zip(a,b):
    result[i]=j
    
print(result)