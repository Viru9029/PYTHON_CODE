#Consecutive characters frequency

def consective_ch_freq(word):
    count = 1
    length =""
    list1 = []
    for i in range(1,len(word)):
       if word[i-1]==word[i]:
          count+=1
       else :
           list1.append(count)
           #length = length + word[i-1]+" repeats "+str(count)+", "
           count=1
    print(list1)

str="geekksforgggeeks"
consective_ch_freq(str)
