# Clean up the words

def clean_up(str):
    new_str = ''
    for i in range(len(str)):
        if str[i].isalpha():
            new_str += str[i]
        elif not new_str.endswith(' ') or i == 0:
            new_str += ' '
    return new_str
print(clean_up("Καλωσήρθες") == "Καλωσήρθες")   # True
# True