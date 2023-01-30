"""for i in range(13):
    print(i * '+')
for j in range(13,1,-1):
    print(j * '*')"""

side = 7
height = list(range(side)) + list(reversed(range(side-1)))
#print(side,'\n', height)
pattern = '{: <{space}}{:+<{val}}'
#print(pattern)
for x in height:
    #print('x =', x)
    a = side - x - 1
    #print('a = ', a)
    b = x * 2 + 1
    #print('b = ', b)
    print(pattern.format('', '', space=a, val=b))