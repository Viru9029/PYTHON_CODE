#multiplication of all the element in the list


def multi_all_element(list):
    sum = 1
    for i in list:
        sum = sum * i
    print(sum)

list1 = [1,2,3]
multi_all_element(list1)