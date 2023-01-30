#smallest largest second smallest second largest no find in the list


def small_largest_elemt(list):
    list.sort()
    print(list)
    smallest_element = list[0]
    second_smallest_element = list[1]
    largest_element = list[-1]
    second_largest_element = list[-2]
    print(smallest_element," ",second_smallest_element," ",largest_element," ",second_largest_element)

l1 = [10,20,30,5,97,39,42,99,75,6,9,2,99,33,89,63,58,99,3598,6,9,63,8,9,63,5,96,3,9,5,36,9,23,9,93,6]
small_largest_elemt(l1)