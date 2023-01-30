values = []
keys = []
a = ord('a')
for i in range(1,27):
    b = chr(a)
    keys.append(b)
    values.append(i)
    a += 1

print(keys)
print(values)

dictionary = dict(zip(keys,values))
print(dictionary)


def sum_of_words(str):
    split_word = str.split()
    sum = []
    for i in range(len(split_word)):
        count = 0
        present_word = split_word[i]
        for j in range(0,len(present_word[i])):
            print(len(present_word[i]))
            print(present_word[j])
            if present_word[j] in dictionary:
                count += dictionary.get(present_word[j])
            sum.append(count)
    print(sum)

stringss = 'i am boss'
sum_of_words(stringss)