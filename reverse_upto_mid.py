str = "helloello0"


def revese_midd(stringsss):
    first = stringsss[:int(len(stringsss) / 2)]
    mid = stringsss[int(len(stringsss) / 2):int(len(stringsss) / 2) + 1]
    last = stringsss[int(len(stringsss) / 2) + 1:]
    output = first[::-1] ," " + mid , " " + last[::-1]
    print(output)


revese_midd(str)
