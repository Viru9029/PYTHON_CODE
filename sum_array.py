#find sum of array


def sum_of_array(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)

list1 = [1,2,3,4,5,6,7,8,9,10]
sum_of_array(list1)