# remove empty tuple form list

def remove_tuple(list):
    list_without_tuple = []
    for i in list:
        if i:
            list_without_tuple.append(i)
    print(list_without_tuple)


list1 = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
remove_tuple(list1)
