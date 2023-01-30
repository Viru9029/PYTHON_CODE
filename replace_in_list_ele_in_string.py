#     original string is : geeksforgeeks is best
# The String after performing replace: ge*k*fo*ge*ks is best
from os import replace


test_list = [2, 4, 7, 10]
test_str = 'geeksforgeeks is best'
repl_char = '*'


def replace_specific_index_no(str, sep_list, replace_item):
    a = list(test_str)
    for i in sep_list:
        a[i] = replace_item
    print(''.join(a))


replace_specific_index_no(test_str, test_list, repl_char)

#************Second Way *******************************
convert_list = list(test_str)
a = [repl_char if index in test_list else ele for index, ele in enumerate(convert_list)]
print(''.join(a))
