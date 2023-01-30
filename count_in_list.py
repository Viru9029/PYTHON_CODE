#
# Program to print duplicates from a list of integers
# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

def duplicates_in_list(list1):
    unique_in_list = list(set(list1))
    dupli_list = []
    for j in unique_in_list:
        if list1.count(j) > 1:
            dupli_list.append(j)
    print(unique_in_list)
    print(dupli_list)


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicates_in_list(list1)
