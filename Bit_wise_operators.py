#Bit-wise operators
"""

2^10  2^9  2^8  2^7   2^6  2^5   2^4   2^3  2^2  2^1  2^0
  |    |    |    |     |    |    |      |    |    |    |
1024  512  256  128   64   32    16     8    4    2    1

"""
#Use of "AND(&)" operator :
"""
input1  input2   Output
1        1        1
0        0        0
1        0        0
0        1        0
"""
a = 50
b = 10
ans = a & b
print(ans)#2
print("\n")

#Use of "OR(|)" operators :
"""
input1  input2   Output
1        1        1
0        0        0
1        0        1 
0        1        1
"""
c = 54
d = 65
ans = c | d
print(ans)#119
print("\n")

#Use of "XOR(^) operators :
"""
input1  input2   Output
1        1        0
0        0        0
1        0        1 
0        1        1
"""
e = 26
f = 87
ans = e ^ f
print(ans)#77
print("\n")

#Use of <<(left shit operators) :
a = 20
ans = a << 2
print(ans)#80
print("\n")
"""
20 binaray is : 00010100
remove left side two dight ahe shift to right side then 01010000 then output is 80

"""

#Use of >> (right shit operators) :
b = 20
ans = b >> 2
print(ans)#5
"""
20 binaray is : 00010100
remove right side two dight ahe shift to left side then 00000101 then output is 5

"""
