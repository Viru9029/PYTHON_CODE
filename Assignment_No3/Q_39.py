#39.Write a Python program to display a number with a comma separator 
def comma_seperated(no):
    print('Original No : {0}'.format(no))
    print('Result no : {:,}'.format(no))



try:
    numbers = int(input('Enter the number : '))
    comma_seperated(numbers)
except:
    print('Please Enter the Interger No')