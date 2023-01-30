"""def main():
    d = {}
    d["jon"] = 22
    d["jbob"] = 22
    d["tom"] = 22
    d["rob"] = 22
    return len(d)
print(main())"""

a = [1,2,3,4,5]
print(a[-1:])

def printHello():
    print("Hello")
a = printHello()

print(hex(15))

c = {}
c[2] = 1
c[1]=[2,3,4]
print(c[1][1])

f = set()
print(type(f))

def f1():
    x = 100
    print(x)
x =+ 1
print(f1())

for i in [1,0]:
    print(i+1)


import math
print(math.pow(3,2))

age = 19
if age < 18:
    print("cannot")
elif age >= 18:
    print("can")

l1 = [1,2,3,[4]]
l2 = list(l1)
print(id(l1) == id(l2))

x = 50
def func():
    global x
    print('x is ',x)
    x = 2
    print('changed global x to ',x)
func()
print('value of x is ',x)

x = 'abcdef'
i = 'a'
while i in x:
    x = x[:-1]
    print(i,end="")

t = [1,2,4,3,8,9]
x = [t[i] for i in range(0,len(t),2)]
print(x)

"""d = {"Shubham":40,"prasad":45}
d["susan"]"""

x = [12,34]
print(len(''.join(list(map(str,x)))))

def power(x,y=2):
    r = 1
    for i in range(y):
        r = r * x
    return r
print(power(3))
print(power(3,3))

print("xyyzxyzxzxyy".count('xyy',2,11))

test = {1:'a',2:'b',3:'c'}
test = {}
print(len(test))

def f(value,values):
    v=1
    values[0]=44
t=3
v=[1,2,3]
f(t,v)
print(t,v[0])