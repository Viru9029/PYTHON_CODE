# 17.	Write a Python script that takes input from the user and displays that input back in upper and lower cases
def change_case(strings,case_no):
    if case_no == 1:
        print('Result : ',strings.lower())
    elif case_no == 2:
        print('Result : ',strings.upper())
    else:
        print('Case no not entered.Please enter case no.')

strings,case_no = input('Note : Enter comma separated inputs.First enter string and then enter case no:\
 \nCase Type : \n1.Lower Case \n2.Upper Case \nEnter the inputs : ').split(',')
change_case(strings,int(case_no))