#String slicing in Python to check if a string can become empty by recursive deletion

# Input  : str = "GEEGEEKSKS", sub_str = "GEEKS"
# Output : Yes
# Explanation : In the string GEEGEEKSKS, we can first 
#               delete the substring GEEKS from position 4.
#               The new string now becomes GEEKS. We can 
#               again delete sub-string GEEKS from position 1. 
#               Now the string becomes empty.


# Input  : str = "GEEGEEKSSGEK", sub_str = "GEEKS"
# Output : No
# Explanation : In the string it is not possible to make the
#               string empty in any possible manner.

def from_string_remove_substring(str,substring):
    index1 = str1.split('GEEKS')
    rem_str = "".join(index1)
    res = ['True' if rem_str == substring else 'False']
    print("".join(res))
    
str1 = "GEEGEEKSSGEK"
sub = 'GEEKS'
from_string_remove_substring(str1,sub)