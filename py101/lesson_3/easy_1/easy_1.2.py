# Easy 1.2

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation(string):
    """
    This function checks if the string ends with an exclamation mark.
    """
    if string[-1] == "!":
        return True
    else:
        return False
    
print(exclamation(str1))  # True
print(exclamation(str2))  # False