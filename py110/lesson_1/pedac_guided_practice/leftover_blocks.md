## Leftover Blocks
You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

- The building blocks are cubes.
- The structure is built in layers.
- The top layer is a single block.
- A block in an upper layer must be supported by four blocks in a lower layer.
- A block in a lower layer can support more than one block in an upper layer.
- You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.

## P: Problem
- Input: integer that represents the number of available blocks
- Output: integer that represents the number of blocks left over 

- Explicit Rules:
    - each block is a cube
    - build the tallest possible structure with the available blocks
    - the top layer is one block (cube) 
    - each upper layer is supporter by 4 blocks (cubes) in the layer before
    - lower layer block can support more than one upper layer block 
    - no gaps

- Implicit Rules:
    - no blocks is none left over
    - can only have integers as the input 


- Mental Model:
    - layers -> # blocks / layer -> total required blocks
        1: 1, 1
        2: 4, 5
        3: 9, 14
        4: 16, 30
    - each layer has layer*layer number of blocks
        - first layer has 1*1 = 1 blocks
        - second layer has 2*2 = 4 blocks
    - total number of blocks required is the sum of each layer including the current one 

# E: Examples and Test Cases
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

# D: Data Structures
- list where each element is the number of blocks for that layer
[1, 4, 9, 16 ...] depicts each layer from top to bottom 
- list to determine the total of blocks required to create x number of layers
[1, 5, 14, 30 ... ] depics the required blocks to complete each level 

# A: Algorithm
1. Start with:
    - set variable remaining blocks equal to input
    - set current layer = 0 

2. If current layer * current layer >= remaining blocks and remaining blocks is not 0 
    - calculate required blocks by multiplying current layer * current layer
    - Subtract required blocks from remaining blocks
    - Increase current layer 
    - Repeat this step
3. Return remaining blocks 
