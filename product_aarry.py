# [1,2,3,4] -> [24,12,8,6]

arr = [1, 2, 3, 4]


def product_array(arr):
    n = len(arr)
    right, left = [1] * n, [1]*n
    prod_array = []
    for i in range(1, n):
        left[i] = left[i-1] * arr[i - 1]
        print('left', left[i])

    for j in range(1, n):
        right[j] = right[j-1] * arr[::-1][j-1]
        print('right', right[j])

    for k in range(n):
        prod_array.append(left[k] * right[::-1][k])
    print(left)
    print(right)
    return print(prod_array)


product_array(arr)
