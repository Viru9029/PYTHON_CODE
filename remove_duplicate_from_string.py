# Remove all duplicates from a given string in Python
#
# Input : geeksforgeeks
# Output : efgkors


def duplicate_in_string(string):
    list1 = set(string)
    print(''.join(list1))

Input = 'geeksforgeeks'
duplicate_in_string(Input)