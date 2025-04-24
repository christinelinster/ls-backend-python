## Running Totals
Write a function that takes a list of numbers and returns a list with the same number of elements, 
but with each element's value being the running total from the original list.

## P : Problem
- Inputs: list of numbers
- Outputs: list of numbers (running totals)
- Explicit Rules:
    - same number of elements
    - sum of itself + any previous elements
    - new list 
- Implicit Rules:
    - only integers and positive numbers > 0 
    - empty lists should return empty list 
    - one element returns one element 
- Mental Model 
    - Initial prefix sum should be 0 
    - Keep track of prefix sum at each iteration
    - Add to new list 

## E: Examples and Test Cases
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

## D: Data Structures:
- List
- Single variable to keep track of prefix

## A: Algorithm:
- Set prefix to 0 
- Set prefix_list = []
- Iterate through current list
- Add prefix to current number
- update prefix
- Add the sum to prefix_list
