#Count occurrences of an element in a list

#Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
#Output: 3


def occ_element(list,x):
    count = 0
    for i in range(len(list)):
        if x == list[i]:
            count += 1
    print(count)

list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
occ_element(list1,10)