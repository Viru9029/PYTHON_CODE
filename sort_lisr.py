# Sort String list by K character frequency
# Input : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”], K = ‘s’ 
# Output : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’] 
# Explanation : bessst has 3 occurrence, geeksforgeekss has 3, and so on.

# Input : test_list = [“geekforgeekss”, “is”, “bessst”], K = ‘e’ 
# Output : [“geekforgeekss”, “bessst”, “is”] 
# Explanation : Ordered decreasing order of ‘e’ count. 


def sort_asc_list(list1):
    list1.sort()
    print(list1)
    
    
lis = ['geekforgeekss', 'is', 'bessst', 'for', 'geeks']
K = 's'   
sort_asc_list(lis)