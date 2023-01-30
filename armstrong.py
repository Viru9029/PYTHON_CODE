#print thr number is armstrong or not

# def armstrong(a):
#     a=a
#     temp = a
#     len_of_val = len(str(a))
#     sum = 0
#     while a != 0:
#         first = a % 10
#         sum = sum + (first**len_of_val)
#         a = a // 10
#         if temp == sum:
#             print("ArmStrong No")
#             break
#         else:
#             print('Not ArmStrong No')
#             break
#
# a = float(input("Enter the number : "))
# armstrong(a)

n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")