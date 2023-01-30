#find length of list


def leng_list(list):
    counter = 0
    for i in list:
        counter += 1
    print(counter)


list1 = [10,20,1,0,1,2,6,9,8,5,3,8,2,6,98,8,2,6,8,7,5]
leng_list(list1)


print(len(list1))