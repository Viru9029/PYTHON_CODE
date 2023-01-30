test_str = "GeeksfoorrGeeks"

def max_freq_char(string):
    tuple1 = tuple(string)
    list1 = []
    for i in tuple1:
        list1.append(0)
    dictinary = dict(zip(tuple1,list1))
    for j in range(len(tuple1)):
        if tuple1[j] in dictinary.keys():
            dictinary[tuple1[j]] += 1
    print(dictinary)
    res = max(dictinary.values())
    a = [k for k in dictinary if dictinary[k] == res]
    print(a)
    list3 = []
    list4 = []
    for key,value in dictinary.items():
        list3.append(key)
        list4.append(value)
    for i in range(len(list4)):
        if list4[i] == res:
            print("This is least no repeted word : ",list3[i])
        else:
            continue


max_freq_char(test_str)

# all_freq = {}
# for i in test_str:
#  if i in all_freq:
#   all_freq[i] += 1
#  else:
#   all_freq[i] = 1
# res = max(all_freq, key = all_freq.get)