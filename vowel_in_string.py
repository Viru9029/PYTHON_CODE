#Program to accept the strings which contains all vowels.

# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'a','i','u' are not present
#
# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present


def string_contain_all_vowels_or_not(string):
    word_separate = list(string)
    vowles = ['a','e','i','o','u','A','E','I','O','U']
    present_vowles = []
    for i in range(len(word_separate)):
        if word_separate[i] in vowles:
            present_vowles.append(word_separate[i].lower())

    unique_vowles = list(set(present_vowles))
    unique_vowles.sort()
    print("Find vowels in string is : ",unique_vowles)
    vowles_lower = ['a','e','i','o','u']
    if unique_vowles == vowles_lower:
        print("Accepted")
    else:
        print("Not Accepted")


list2 = 'geeksforgeeks'
string_contain_all_vowels_or_not(list2)

