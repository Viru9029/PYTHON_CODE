

def swap_list(list):
    temp = list[0]
    list[0]=list[2]
    list[2]=temp
    print(list)

List1 = [23, 65, 19, 90]
print(swap_list(List1))