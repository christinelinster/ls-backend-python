# Leftover Blocks 
'''
1. Start with:
    - set variable remaining blocks equal to input
    - set current layer = 1

2. If current layer * current layer >= remaining blocks and remaining blocks is not 0 
    - calculate required blocks by multiplying current layer * current layer
    - Subtract required blocks from remaining blocks
    - Increase current layer 
    - Repeat this step
3. Return remaining blocks 

'''

def calculate_leftover_blocks(blocks):
    remaining_blocks = blocks
    curr_layer = 1
    

    while remaining_blocks >= curr_layer ** 2:
        required_blocks = curr_layer ** 2
        remaining_blocks -= required_blocks
        curr_layer += 1

    return remaining_blocks


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True