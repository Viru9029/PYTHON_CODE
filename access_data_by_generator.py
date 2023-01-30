# def data_access(path):
#     with open(path,'r') as data:
#         for i in data.read():
#             yield i


# path = 'V:\\CDAC_ALL_SUB\\1.Python\other\\large_file.txt'
# print(next(data_access(path)))


# def read_data(file_object, chunk_size=1024):
#     """Lazy function (generator) to read a file piece by piece.
#     Default chunk size: 1k."""
#     while True:
#         data = file_object.readlines()
#         if not data:
#             break
#         yield data


# path = 'V:\\CDAC_ALL_SUB\\1.Python\other\\large_file.txt'
# with open(path) as f:
#     for piece in read_data(f):
#         print(piece)

def data_access(path):
    with open(path, 'r', encoding="utf8") as file_data:
        read_file = file_data.read().split('\n')
        for i in read_file:
            yield i


path = 'V:\\CDAC_ALL_SUB\\1.Python\other\\large_file.txt'

for j in data_access(path):
    print(j)

# # 1.  Write a Python program to read first n lines of a file.
# n = int(input("Enter the Number to read lines upto : "))
# file = open("Readable_File.txt", "r")
# read_file = file.read().split("\n")
# count = 0
# # file.seek(0)
# for i in read_file:
#     count += 1
#     print(i)
#     if count == n:
#         break
#     else:
#         pass
#     file.close()
