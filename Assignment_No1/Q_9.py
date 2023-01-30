# 9.	Accept number of rows and columns form end user and print following pattern e.g. if row = 5 and column = 5 then
# *****
# *****
# *****
# *****
# *****

def rows_colums_pattern(rows,column):
    if rows <= 0 or column <= 0:
        return print('Please Enter the Positive No')
    else:
        for i in range(rows):
            print("*"*column)
    
try:
    rows,column=list(map(int,input('Enter first no of rows then no of colums Note: Enter Space separated values :').split()))
    rows_colums_pattern(rows,column)
except:
    print('Please Enter the Integer No')