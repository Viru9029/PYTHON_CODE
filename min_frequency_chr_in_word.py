#Least Frequent Character in String

test_str = "GeeksfoorrGeeks"

def least_freq_char(string):
    tuple1 = tuple(string)
    list1 = []
    for i in tuple1:
        list1.append(0)
    dictinary = dict(zip(tuple1,list1))
    for j in range(len(tuple1)):
        if tuple1[j] in dictinary.keys():
            dictinary[tuple1[j]] += 1
    print(dictinary)
    res = min(dictinary.values())
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


least_freq_char(test_str)