#Python – Ways to remove multiple empty spaces from string List
# The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
# List after filtering non-empty strings : ['gfg', 'is', 'best']


test_str = ['gfg', '   ', ' ', 'is', '            ', 'best']

def remove_empty_spaces(str):
    adter_list = []
    for i in str:
        if i.strip():
            adter_list.append(i)
    print(adter_list)

remove_empty_spaces(test_str)


#**********second way**********************

a = [ele for ele in test_str if ele.strip()]
print(a)