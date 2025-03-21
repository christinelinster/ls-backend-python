# Short Long Short 

def short_long_short(str1, str2):
    longer = str1 if len(str1) > len(str2) else str2
    shorter = str1 if len(str1) < len(str2) else str2

    return (shorter + longer + shorter)

# These examples should all print True
print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh'))
print(short_long_short('', 'xyz'))