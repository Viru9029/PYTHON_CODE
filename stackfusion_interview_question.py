import os

path = 'V:\\CDAC_ALL_SUB\\1.Python\\other\\Just_for_Pratices'

index_list = os.listdir(path)
#print(index_list)

def list_name(dir_list):
    for i in dir_list:
        a = i.split('_')
        yield a[3]


#print(next(list_name(index_list)))
#name = []
for j in list_name(index_list):
    print(j)
    #name.append(j)
    
#print(name)
