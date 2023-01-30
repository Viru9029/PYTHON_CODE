capial_char = ord('A')
small_char = ord('a')
capial_char_list = []
small_char_lsit = []
int_value = []
for i in range(0,26):
    cap = chr(capial_char)
    small = chr(small_char)
    capial_char_list.append(cap)
    small_char_lsit.append(small)
    int_value.append(i)
    capial_char = capial_char+1
    small_char = small_char+1

print(capial_char_list)
print(small_char_lsit)
print(int_value)



print(chr(65))
print(ord('A'))