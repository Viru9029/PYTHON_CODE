l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from functools import reduce
sum = reduce(lambda x,y : x+y,l1)
print(sum)