#find Cumulative sum of a list

# Input : list = [10, 20, 30, 40, 50]
# Output : [10, 30, 60, 100, 150]


def cumulative_sum(list):
    cumm_sum = []
    cumm_sum.append(list[0])
    for i in range(1,len(list)):
        sum = cumm_sum[-1] + list[i]
        cumm_sum.append(sum)
    print(cumm_sum)


list1 = [10, 20, 30, 40, 50]
cumulative_sum(list1)
