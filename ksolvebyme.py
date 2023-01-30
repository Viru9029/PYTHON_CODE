def student_selection(marks,k):
    sorted_marks = sorted(marks) # To sort the array in ascending order
    print(marks)
    if k==1:
        return sorted_marks[-1]
    else:
        min_diff=[]
        for i in range(0,len(sorted_marks)-(k-1)):
            diff= sorted_marks[i+(k-1)]-sorted_marks[i]
            min_diff.append(diff)
            if (i+k) == sorted_marks[-1]:
                break
        print("\n",sorted(min_diff))
        
        for i in range (0,len(sorted_marks)-1):
             if (sorted_marks[i+(k-1)] - sorted_marks[i]) == sorted(min_diff)[0]:
                print("\n Selected Students are : ", sorted_marks[i:k])
                break

# Driver code
if __name__=="__main__":
    n=int(input("\n Enter the number of students in the class : "))
    marks=list(map(int,input("\nEnter the marks : ").strip().split()))[:n]
    k=int(input("\n How many students you want to select : "))

    student_selection(marks,k)

    
