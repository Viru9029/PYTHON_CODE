#to interchange first and last elements in a list


list1 = [12, 35, 9, 56, 24]

def change_fist_last_ele(list1):
    first = list1[:1]
    last = list1[-1:]
    list1[:] = last + list1[1:len(list1)-1] + first
    print(list1)

change_fist_last_ele(list1)


