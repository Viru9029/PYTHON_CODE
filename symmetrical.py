# Python program to check whether the string is Symmetrical or Palindrome
#
# Input: khokho
# Output:
# The entered string is symmetrical
# The entered string is not palindrome
#
# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome


def symmetrical(a):
    n = len(a)
    if n % 2==0:
        mid = (n // 2)+1
        print(mid)
    else:
        mid = n // 2
        print(mid)

    while True:
        if a[:mid-1] == a[mid-1:]:
            print("string is symmetric")
            break
        else:
            print('string not symmetric')
            break

b='amaama'
symmetrical(b)