# UTF-16 String Value

def utf16_value(str):
    sum = 0
    for letter in str:
        sum += ord(letter)
    return sum

OMEGA = "\u03A9"
print(utf16_value(OMEGA))
print(utf16_value(OMEGA + OMEGA + OMEGA))