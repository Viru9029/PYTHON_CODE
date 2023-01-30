# positive no in given list

def positive_no(list):
    positive_no_list = []
    for i in list:
        if i > 0:
            positive_no_list.append(i)
        else:
            continue
    print(positive_no_list)


list1 = [12, -7, 5, 64, -14]
positive_no(list1)
