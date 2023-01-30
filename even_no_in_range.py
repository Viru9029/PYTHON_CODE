# all even no in given range

def even_no_in_range(x,y):
    even_no = []
    for i in range(x,y):
        if i % 2 == 0:
            even_no.append(i)
    print(even_no)

even_no_in_range(4,15)