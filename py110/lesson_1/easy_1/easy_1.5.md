## Letter Counter (Part 1)
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

## P: Problem
- Inputs: string of words
- Outputs: dictionary with key as length of word, and value as frequency of words with that length 
- Explicit Rules:
    - words are space separated 
    - punctuation counts as a letter 
    - strings can be empty 
- Implicit Rules:
    - empty string should return empty dictionary
- Mental Model
    - check length of each word in the string
    - use length as dictionary key
    - check if dictionary has that key, otherwise add size as the key with value as frequency

## E: Examples and Test Cases

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

## D: Data Structure
- list with each word as its own element
- dictionary with key as size, value as frequency of size

## A: Algorithm
- Set list_string, list to capture each space-separated word
- Set empty dict word_count 
- Iterate through each word in the list:
    - get length of word
    - if not in word_count, then set size of word as key, value as 1
    - if in word_count, add 1 to existing value 

