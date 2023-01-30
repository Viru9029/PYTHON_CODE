#even no in the list


def even_no(list):
    even_no_list = []
    for i in list:
        if i % 2 ==0:
            even_no_list.append(i)
        else:
            continue
    print(even_no_list)

list = [2,0, 7, 5, 64, 14]
even_no(list)

