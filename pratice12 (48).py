def is_leap(year):
    leap = True
    non_leap = False
    if year % 400 == 0 and year % 100 == 0:
        print(leap)
        return True
    elif year % 4 == 0 and year % 100 != 0:
        print(leap)
        return True
    else:
        return non_leap



year = int(input())
print(is_leap(year))