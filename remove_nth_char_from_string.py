#Remove the ith character from the string using the native method

def remove_chr(a,n):
    print(len(a))
    string = a.replace(n,'',1)
    print(string)


remove_chr("GeeksForGeeks",'s')

def remove_chr_by_index_no(a,n):
    while n <= len(a)-1:
        first = a[:n]
        second = a[n+1:]
        final = first + second
        print(final)
        break
    else:
        print('Please enter valid index no')

remove_chr_by_index_no("GeeksForGeeks",0)