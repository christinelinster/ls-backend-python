# Palindromic Strings (Part 1)

'''
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. 
A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

'''

def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)