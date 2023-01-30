def check_sum(nums, k):
    list1 = []
    for i in range(len(nums)):
        if nums[i] == k:
            return 'true'
        for j in range(nums[i], len(nums)):
            if nums[j] == k:
                return 'true'
            elif (nums[i] + nums[j]) == k:
                list1.append(i)
                list1.append(j)
                print(list1)
                return 'true'
            else:
                return 'false'
    print(list1)


lis = [23,2, 4, 7]
k = 13
print(check_sum(lis, k))
