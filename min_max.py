#min max code

def maximumChars(str):
    n = len(str)
    res = -1
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (str[i] == str[j]):
                res = max(res, abs(j - i - 1))
                print(res)
    return res

print(maximumChars('aabaaaaaaaaaaaaaabaaab'))




def minmax(str):
    seperate_word = list(str)
    lista = []
    lisrb = []
    for i in range(0,len(seperate_word)):
        if seperate_word[i] == 'a':
            lista.append(i)
        else:
            lisrb.append(i)
    x = (lista[-1] - lista[0])
    y = (lisrb[-1] - lisrb[-2])
    result = x + y
    return result

print(minmax('aabaaaaaaaaaaaaaabaaab'))

# a="aabaaaaaaaaaaaaaabaaab"
# c=[]
# d=[]
# bb=[]
# l1=[]
#
# for i in range(0,len(a)):
#     c.append(a[i])
#     if a[0]==a[i]:
#         c.append(i)
#     if a[0]!=a[i]:
#         bb.append(i)
#
# x=bb[-1]-bb[-2]
# for i in range(0,len(bb)):
#    final= bb[-1]-bb[-i]
#    l1.append(final)
# l1.sort()
# y=l1[1]
# print(x+y)