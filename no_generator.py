def genrator_no(n):
    count = 10
    while count != n:
        yield count
        count += 1


for i in genrator_no(16):
    print(i)
