# When will I retire? 

from datetime import datetime 

age = int(input('What is your age? '))
retire = int(input('When would you like to retire? '))

curr_year = datetime.now().year
time = retire - age
retirement_age = curr_year + time

print(f'It\'s {curr_year}. You will retire in {retirement_age}.')
print(f'You have only {time} years to go.')