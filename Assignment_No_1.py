# #1.	Accept number of rows from end user and print * asterisk on each row. E.g. if input is 5 then
# *
# *
# *
# *
# *


# def print_asterisk(user_input):
#     if user_input <= 0:
#         return print('Please Enter Positive No')
#     else:
#         for i in range(0,user_input):
#             print('*')


# try:
#     print_asterisk(int(input('Enter the number of rows : ')))
# except:
#     print('Please Enter the Integer No')

###################################################################################################################
# 2.	Accept number of rows from end user and print following * asterisk pattern ( right angle triangle )
# *
# **
# ***
# ****
# *****

# def right_angle_triangle_pattern(n):
#     if n <= 0:
#         return print('Please Enter Positive No')
#     else:
#         for i in range(0,(n+1)):
#             print('*'*i)

# try:
#     right_angle_triangle_pattern(int(input('Enter the number of rows : ')))
# except:
#     print('Please Enter the Integer No')
################################################################################################################
# 3.	Accept number of rows from end user and print following * asterisk pattern ( inverted right-angle triangle )
# *****
# ****
# ***
# **
# *

# def inverted_right_angle_triangle_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(0,n+1):
#             print('*'*(n-i))

# try:
#     inverted_right_angle_triangle_pattern(int(input('Enter the number of rows : ')))
# except:
#     print('Please Enter the Integer No')

###################################################################################################################
# 4.	Accept number of rows from end user and print following * asterisk pattern ( equilateral triangle )
#     *
#    ***
#   *****
#  *******

# def equilaterial_triangle_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(n):
#             print(" "*(n-i),"*"*(2*i+1))

# try:
#     equilaterial_triangle_pattern(int(input('Enter the number of rows : ')))
# except:
#     print('Please Enter the Integer No')

# ##################################################################################################################

# 5.Accept number of rows from end user and print following * asterisk pattern (( inverted equilateral triangle ))
# *******
#  *****
#   ***
#    *

# def inverted_equilateral_trangle_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(n,-1,-1):
#             print(" "*(n-i),"*"*(2*i+1))

# try:
#     inverted_equilateral_trangle_pattern(int(input('Enter the no of rows : ')))
# except:
#     print('Please Enter the Integer No')

# #####################################################################################################################
# 6.	Accept number of rows from end user and print following * asterisk pattern ( full diamond )
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *

# def diamnond_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(n):
#             print(" "*(n-i),"*"*(2*i+1))
#         for j in range(n-2,-1,-1):
#             print(" "*(n-j),"*"*(2*j+1))

# try:
#     diamnond_pattern(int(input('Enter the number of rows : ')))
# except:
#     print('Please Enter the Integer No')

# ############################################################################################################
# 7.	Accept number of rows from end user and print following * asterisk pattern ( half diamond – right )
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# def half_diamond_right_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(n+1):
#             print("*"*i)
#         for j in range(n-1,-1,-1):
#             print("*"*j)

# try:
#     half_diamond_right_pattern(int(input('Enter the no of rows : ')))
# except:
#     print('Please Enter the Integer No')

# ######################################################################################################################

# 8.	Accept number of rows from end user and print following * asterisk pattern ( half diamond – left )
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

# def half_diamond_left_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(n+1):
#             print(" "*(n-i),"*"*i)
#         for j in range(n-1,-1,-1):
#             print(" "*(n-j),"*"*j)

# try:
#     half_diamond_left_pattern(int(input('Enter the no of rows : ')))
# except:
#     print('Please Enter the Integer No')

# ###########################################################################################################

# 9.	Accept number of rows and columns form end user and print following pattern e.g. if row = 5 and column = 5 then
# *****
# *****
# *****
# *****
# *****

# def rows_colums_pattern(rows,column):
#     if rows <= 0 or column <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(rows):
#             print("*"*column)
    
# try:
#     rows,column=list(map(int,input('Enter first no of rows then no of colums Note: Enter Space separated values :').split()))
#     rows_colums_pattern(rows,column)
# except:
#     print('Please Enter the Integer No')

# ################################################################################################################
# 10.	Accept number of rows from end user and print following * asterisk pattern
#   *******
#    *****
#     ***
#      *
#     ***
#    *****
#   *******
# def half_half_diamond_pattern(n):
#     if n <= 0:
#         return print('Please Enter the Positive No')
#     else:
#         for i in range(n-1,-1,-1):
#             print(" "*(n-i),"*"*(2*i+1))
#         for j in range(1,n):
#             print(" "*(n-j),"*"*(2*j+1))

# try:
#     half_half_diamond_pattern(int(input('Enter the no of rows : ')))
# except:
#     print('Please Enter the Integer No')

# ##############################################################################################
