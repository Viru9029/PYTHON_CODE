#38.Write a Python program to print the following integers with '*' to the right of the specified width 
def specified_star(no,width_star):
    print('Original No : {0}'.format(no))
    print('Result No : ',str(no)+'*'*width_star)


try:
    numbers = int(input('Enter the number : '))
    width = int(input('Enter the width of left zeros : '))
    specified_star(numbers,width)
except:
    print('Please Enter the Interger No')