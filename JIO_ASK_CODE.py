

l1=[]
l2=[]
l3=[]
final=[]
char1_start=ord('A')
char_start=ord('a')
a=input("enter your name or string:")
for i in range(1,27):
    p=chr(char_start)
    k=chr(char1_start)
    l1.append(p)
    l2.append(i)
    l3.append(k)
    char1_start=char1_start+1
    char_start=char_start+1

a = a.lower()
split_output = a.split()
print(split_output)

for i in range(len(split_output)):
    sum = 0
    for j in range(len(split_output[i])):
        present = split_output[i]
        for k in range(len(l1)):
            if present[j] == l1[k]:
                sum = sum + l2[k]
    final.append(sum)
               
# #sorted_array = np.sort(final)
# print("this is final answer:",#sorted_array)