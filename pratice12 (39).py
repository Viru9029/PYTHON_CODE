for i in range(0, 11):
    print("\t",(i),end="")
print()
print("\t","+"+"-" * 80 , end="")
print()
for x in range(1, 11):
    print(x * 1,"\t","|","\t",end="")
    for y in range(1, 11):
        z=x*y
        print(z,"\t", end="")
    print()