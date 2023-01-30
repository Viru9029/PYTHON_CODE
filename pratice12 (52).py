string_name = input("Enter the string name : ")
#string_name = "amaama"
half = int(len(string_name)/2)

#symmertical
if int(len(string_name)) % 2 == 0: #EVEN no string
    first_half = string_name[:half]
    second_half = string_name[half:]
else: #ODD no string
    first_half = string_name[:half]
    second_half = string_name[half+1:]

if first_half == second_half:
    print("String is symmetrical")
else:
    print("String not symmetrical")

#palindrome
if string_name == string_name[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")