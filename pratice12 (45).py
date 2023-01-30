nums = [2,7,11,15]
target = 9
for i in range(int(len(nums))):
    if nums[i] <= target:
        first_value=nums[i]
        store_values = []
        store_values.append(i)
        print()
        print(store_values)


for j in range(int(len(nums))):
    if nums.index([j]) <= target:
        first_value1 = j
        print(j)
        #store_values1 = []
        #store_values1.append(j)
        #print(store_values1)

T = int(input())
for tc in range(T):
    # Read integers a and b.
    (a, b) = map(int, input().split(' '))

    ans = a + b
    print(ans)