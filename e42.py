


def sum_of_list(lis,n):
    sum = 0
    index = []
    for i in range(0,len(lis)):
        for j in range(0,len(lis)):
            if (lis[i] + lis[j]) == n:
                sum += lis[i] + lis[j]
                index.append(i)
                index.append(j)
                break

    print(sum)
    print(index)


list1 = [2,3,7,11,15]
sum_of_list(list1,9)




# index2 = []
# sum1 = 0
#
# def sum_of_list1(lis,n):
#     lis.sort()
#     index2 = []
#     for i in range(0,len(lis)):
#         if lis[i] <= n:
#             index2.append(i)
#     for i in range(0,len(lis)):
#
#
#
#
#
#
# list1 = [2,3,7,11,15]
# sum_of_list(list1,9)
#
#
# result = filter(lambda x : if x is <=9,list1)
# print(result)