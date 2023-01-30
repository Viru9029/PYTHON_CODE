#String slicing in Python to rotate a string

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee"

def string_slicing(str,d):
    left_rotation = str[d:] + str[:d]
    right_rotation = str[len(str)-d:] + str[:len(str)-d]
    print(left_rotation)
    print(right_rotation)
    
s = "qwertyu"
d = 2
string_slicing(s,d)