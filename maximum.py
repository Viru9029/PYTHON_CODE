#print maximum no in two between two variable


a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

def maximum(a,b):
    if a >= b:
        print(a)
    else:
        print(b)

maximum(a,b)


max_no = max(a,b)
print('maximum no : ',max_no)