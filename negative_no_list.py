#negative no in list


def negative_no_in_list(list):
    negative_list = []
    for i in list:
        if i < 0:
            negative_list.append(i)
        else:
            continue
    print(negative_list)

list1 = [12, -7, 5, 64, -14]
negative_no_in_list(list1)



neg_nos = list(filter(lambda x: (x < 0), list1))
print(neg_nos)