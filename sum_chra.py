l1=[]
l2=[]
l3=[]
final=[]
le_n=[]


char_start=ord('a')
a=input("enter your name or string:")
a=a.lower()
for i in range(1,27):
    p=chr(char_start)
   
    l1.append(p)
    l2.append(i)
 
    
    char_start=char_start+1
b=a.split()
for i in range(0,len(b)):
    result=[]
    for j in range(0,len(b[i])):
        
        
        for k in range(0,26):
            if b[i][j]==l1[k]:
                result.append(l2[k])
    final.extend([result])
for i in final:
    b=sum(i)
    le_n.append(b)
print(sorted(le_n))
            

        
        
                



    

            

           
     
