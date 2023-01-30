#print odd no in list


def odd_no_in_list(list):
    odd_no = []
    for i in list:
        if i % 2 == 0:
            continue
        else:
            odd_no.append(i)
    print(odd_no)
    print(" ".join(odd_no))


list1 = [2, 7, 5, 64, 14]
odd_no_in_list(list1)