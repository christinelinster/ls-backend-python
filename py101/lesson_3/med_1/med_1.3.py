# Med 1.3 

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element) # Mutates List
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element] # Creates and assigns new list 
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer