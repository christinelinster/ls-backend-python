# Running Totals

'''
Write a function that takes a list of numbers and returns a list with the same number of elements, 
but with each element's value being the running total from the original list.
'''

def running_total(list):
    prefix = 0
    prefix_list = [] 

    for num in list:
        prefix += num 
        prefix_list.append(prefix)
    return prefix_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True