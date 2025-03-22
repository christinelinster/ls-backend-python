# Leap Years (Part 2)

year = input('Please provide a year greater than 0: ')

def leap_year(year):
    if year < 1752 and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0
