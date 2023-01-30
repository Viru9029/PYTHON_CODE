#n largest no in list


def nth_largest_no(list,nth_no):
    list.sort()
    print(list)
    largest_no = list[-nth_no:]
    print(largest_no)


l1 = [10,25,6,9,8,89,56,87,5,4,7,58,26,9,8,68,698,2,6,8,3,59,3,59,3,3,8,6,32,58,25,8,2,8,7,88,2,9,2,5,20,5]
nth_largest_no(l1,5)