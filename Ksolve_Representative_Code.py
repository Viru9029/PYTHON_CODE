def Representative(input1,input2,input3):
    sort_list = sorted(input2)
    print("sorted_list : ",sort_list)
    if input3 == 1:
        return print(sort_list[-1])
    else:
        min_diff = []
        for i in range(0,len(sort_list)-(input3-1)):
            min_diff.append(sort_list[i+(input3-1)] - sort_list[i])
            if (i+input3) == sort_list[-1]:
                break
        print("Min_diff : ",sorted(min_diff))
        for i in range(0,len(sort_list)-1):
            if sorted(min_diff)[0] == (sort_list[i+(input3-1)] - sort_list[i]):
                print("Result : ",sort_list[i:(input3)])
                break
            



input1=int(input('Enter the number of student : '))
input2=[int(x) for x in input("Enter the %d students Marks : " %(input1)).split()][:input1]
input3=int(input('Enter the number of representatives selected : '))
Representative(input1,input2,input3)