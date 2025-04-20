# Palindromic Strings (Part 2)

'''
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. 
A palindrome reads the same forwards and backwards. For this problem, it is case-insensitive and only alphanumerics matter.

'''

def is_real_palindrome(text):
    alnum_text = "".join(char for char in text if char.isalnum())
    return alnum_text.casefold() == alnum_text[::-1].casefold()



print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True