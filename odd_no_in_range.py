# odd no in given range


def odd_no_in_range(x,y):
    odd_no_list = []
    for i in range(x,y+1):
        if i % 2 != 0:
            odd_no_list.append(i)
    print(odd_no_list)

odd_no_in_range(4,15)