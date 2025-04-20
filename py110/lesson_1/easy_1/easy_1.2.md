## Palindromic Strings (Part 1)
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

## P: Problem
- Input: string
- Output: Boolean (True or False)
- Explicit:
    - return true if the string is a palindrome (reads the same from both sides)
    - case matters
    - all characters matter (spaces, apostrophes)
- Implicit:
    - empty string is considered a palindrome 

## E: Examples / Test Cases

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

print(is_palindrome('Madam') == False)

print(is_palindrome("madam i'm adam") == False)

## D: Data Structures
- string

## A: Algorithm
- Two pointers
- 1. First variable (left) at first letter in the string (index 0)
- 2. Second variable (right) at last letter in the string (lenth of string - 1)
- 3. REPEAT these steps while left < right:
        - Check if left == right
        - if it is not equal, return False
        - if it is equal:
            - increase left by 1
            - decrease right by 1
- 4. If we are at the end of the loop, that means all checks have passed and we return True 

