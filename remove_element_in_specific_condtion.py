#remove element from the list take any condition


def remove_ele(list):
    remove_elemet = []
    for i in list:
        if i % 2 ==0:
            remove_elemet.append(i)
            list.remove(i)
    print("After removing condition no in list : " ,list)
    print('Removing element in list : ', remove_elemet)



list1 = [12, 15, 3, 10]
remove_ele(list1)