## Searching 101
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

## P: Understand the Problem
    - Input: A number string from user input
    - Output: A string that describes if the 6th number is in the preceding 5 numbers provided 
    
    - Explicit: 
        - six (6) numbers from the user
        - numbers are solicited from the user on six separate occasions, each one specifying which number we are at 
        - compare the last number to the previous 5
    - Implicit: 
        - inputs are saved for comparison 
        - inputs are converted to integer type
        - the user provides a valid number
        - numbers only include a combination of 0-9, Infinity does not count 

## E: Examples and Test Cases
    Example 1: 
        Enter the 1st number: 25
        Enter the 2nd number: 15
        Enter the 3rd number: 20
        Enter the 4th number: 17
        Enter the 5th number: 23
        Enter the last number: 17

        17 is in 25,15,20,17,23.

    Example 2: 
        Enter the 1st number: 25
        Enter the 2nd number: 15
        Enter the 3rd number: 20
        Enter the 4th number: 17
        Enter the 5th number: 23
        Enter the last number: 18

        18 isn't in 25,15,20,17,23.

## D: Data Structures
    - list of integers 
    - keep track of the numbers we have received from the user
    - input with updated prompt 
    - string output 

## A: Algorithms
    - 1. Create a empty list to track the numbers provided 
    - 2. Ask the user for the first number
        - Keep asking the user until they provide a valid number (0-9), no floats are allowed
    - 3. Add the number to the list 
    - 5. Repeat steps 2-3 until we have received 6 numbers 
    - 6. Output whether the 6th number appears in the previous 5 

## C: Implementing a Solution in Code 