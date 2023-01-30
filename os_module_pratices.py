# handling the current working directory
import os

cwd = os.getcwd()
print(cwd)


# make directory through code
# add_dic = 'aaaaaaab'
# parent_dic = 'v:\\CDAC_ALL_SUB\\1.Python\\other'

# add = os.path.join(parent_dic, add_dic)
# os.mkdir(add)
# print(add)

# Listing out Files and Directories with Python

# file_list = os.listdir(cwd)
# print(file_list)

# def file_name(file_list):
#     for i in file_list:
#         yield i
        
# for i in file_name(file_list):
#     print(i)
    
    
#change the current directory
def change_dir():
    a = os.getcwd()
    print(a)

change_dir()
   
print('after changing directory')

os.chdir('../')

change_dir()
