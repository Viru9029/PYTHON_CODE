def sort_fun(lis):
    sort_lis = []
    while lis:
        min = lis[0]
        for i in lis:
            if i < min:
                min = i
        sort_lis.append(min)
        lis.remove(min)
    print(sort_lis)

sort_fun([2,4,5,5,6,7,8,5,343,45,565,67,788,8,89,98,5,4,33,33,3445,45,566,7,55,676,565,567,567,56,465])