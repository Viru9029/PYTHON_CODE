#CONSRCUTIVE VOWELS:
#s = input().strip().lower()
s ='ASIEOPKMGETLOST'
c=0
for i in range(0,len(s)-1):
    if s[i] in 'aeiouAEIOU' and s[i+1] in 'aeiouAEIOU':
        c+=1
print(c)


s ='ASIEOPKMGETLOST'



# #s = input().strip().lower();c=0
# for i in range(len(s)-1):
#     if s[i] in 'aeiou' and s[i+1] in 'aeiou':c+=1
# print(c)