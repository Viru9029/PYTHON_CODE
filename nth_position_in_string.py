# Python program to find the character position of Kth word from a list of strings
# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
# Output : 0
# Explanation : 21st index occurs in “geeks” and point to “g” which is 0th element of word.

# Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 15
# Output : 1
# Explanation : 15th index occurs in “best” and point to “e” which is 1st element of word.

def find_position_of_character(lis, nth):
    list1 = []
    for i in range(0, len(lis)):
        for j in range(0, len(lis[i])):
            list1.append(str(j))
    print(list1)
    if list1[nth]:
        print(list1[nth])
    else:
        print('Index out of range')


test_list = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
K = 21
find_position_of_character(test_list, K)
