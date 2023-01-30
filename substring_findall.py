# Successive Characters Frequency
# Input : test_str = ‘geeks are for geeksforgeeks’, que_word = “geek” Output : {‘s’: 3} 
# Input : test_str = ‘geek’, que_word = “geek” Output : {}
import re
def repeted_substring_count(str,substring):
    index = re.findall(substring,str)
    count = 0
    for i in range(len(index)):
        if index[i] == substring:
            count += 1
    print(substring, ' : ',count)
    
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'
que_word = 'geek'
repeted_substring_count(test_str,que_word)