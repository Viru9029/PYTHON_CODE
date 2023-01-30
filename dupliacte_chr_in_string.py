# Find all duplicate characters in string
#
# Input : hello
# Output : l
#
# Input : geeksforgeeeks
# Output : e g k s

def duplicate_chr_in_string(string1):
    convert = list(string1)
    dictionary = {}
    for i in range(len(convert)):
        dictionary[convert[i]] = dictionary.get(convert[i],0)+1
    print(dictionary)
    res = [i for i in dictionary if dictionary[i] >= 2]
    print("Duplicate characters in string is : ", " ".join(res))


a = 'geeksforgeeeks'
duplicate_chr_in_string(a)