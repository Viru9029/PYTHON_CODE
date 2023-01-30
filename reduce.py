import functools
lis = [1, 3, 5, 500, 1200, 2]
print(functools.reduce(lambda a, b: a if a + b == 4 else b, lis))