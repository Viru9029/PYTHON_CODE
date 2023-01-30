from functools import reduce
arr = [100, 10, 5, 25, 35, 14]
sum_1 = reduce(lambda x, y: x*y, arr)
print(sum_1)

print(sum_1 % 11)