# Easy 3.5 

# Refactor the following code: 

'''
def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
'''

# Option 1 

def is_color_valid(color):
    return color in ['blue', 'green']

# Option 2 
def is_color_valid(color):
    return color == "blue" or color == "green"
