# Get middle character

def center_of(str):
    middle = len(str) // 2
    if len(str) % 2 == 0:
        return (str[middle - 1: middle + 1])
    else:
        return str[middle]
    

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True