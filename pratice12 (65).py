X = [1,5,9,0]
Y = [3,0,2,9]
"""result = set(X).intersection(set(Y))
print(result)"""

print(list([lambda X,Y:set(X).intersection(set(Y))]))
