#  Tip Calculator

bill = int(input('What is the bill? '))
percent = int(input('What is the tip percentage? '))

tip = bill * (percent / 100)
total = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')
