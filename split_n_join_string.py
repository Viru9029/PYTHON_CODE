#Python program to split and join a string

# Split the string into list of strings
#
# Input : Geeks for Geeks
# Output : ['Geeks', 'for', 'Geeks']
#
#
# Join the list of strings into a string based on delimiter ('-')
#
# Input :  ['Geeks', 'for', 'Geeks']
# Output : Geeks-for-Geeks

def split_join_string(string):
    spliting = string.split()
    print(spliting)
    joining = "_".join(spliting)
    print(joining)



stri = 'Geeks for Geeks'
split_join_string(stri)