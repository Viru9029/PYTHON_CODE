#37.Write a Python program to print the following integers with zeros to the left of the specified width 
def intergers_with_zeros(no,spec_width):
    print('Original No : {0}'.format(no))
    #print('Result No : {:0>4d}'.format(no))
    print('Result No : ','0'*spec_width+str(no))

try:
    numbers = int(input('Enter the number : '))
    width = int(input('Enter the width of left zeros : '))
    intergers_with_zeros(numbers,width)
except:
    print('Please Enter the Interger No')