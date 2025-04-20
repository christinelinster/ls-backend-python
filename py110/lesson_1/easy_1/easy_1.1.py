# Searching 101

'''
Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

'''

# Helper functions
def get_suffix(num):
    match num:
        case 1:
            return "1st"
        case 2:
            return "2nd"
        case 3:
            return "3rd"
        case 6: 
            return "last"
        case _: 
            return f"{num}th"
        
def is_valid_number(num):
    return True if num.isdigit() else False

# Get 6 numbers from user
numbers = []
for i in range(1,7):
    num_with_suffix = get_suffix(i)
    user_number = input(f"Enter the {num_with_suffix} number: ")
    
    while not is_valid_number(user_number):
        user_number = input(f"Enter the {num_with_suffix} number: ")

    numbers.append(user_number)

# Get the last number
last_number = numbers.pop()
first_five_numbers = ", ".join(numbers)

# Print results
if last_number in numbers:
    print(f'{last_number} is in {first_five_numbers}')
else:
    print(f'{last_number} is not in {first_five_numbers}')



