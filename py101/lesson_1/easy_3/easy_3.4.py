# String Strings

def stringy(int):
    str = ''
    for i in range(int):
        if(i % 2 == 0):
            str += '1'
        else: 
            str += '0'
    return str

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
