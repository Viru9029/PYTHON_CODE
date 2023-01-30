def sorti(lis):
    res_lis = []
    while lis:
        min = lis[0]
        for i in lis:
            if i < min:
                min = i
        res_lis.append(min)
        lis.remove(min)
    print(res_lis)

sorti([3,67,8,9,9,86,34,2,34,5,6,654,356,6456,36,45635,456,6,66,565,67,67])