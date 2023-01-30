# remove empty list from list

def remove_empty_list(list):
    element = []
    for i in list:
        if i:
            element.append(i)
    print(element)

input_list = [5, 6, [], 3, [], [], 9]
remove_empty_list(input_list)