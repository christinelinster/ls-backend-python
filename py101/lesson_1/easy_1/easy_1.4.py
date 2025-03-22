# How big is the room? 
r_width = int(input('Enter width of the room (in meters): '))
r_length = int(input('Enter length of the room (in meters): '))

square_meters = r_width * r_length

print(f'The area of the room is {square_meters:.2f} square meters')
print(f'The area of the room is {square_meters * 10.7639:.2f} square feet')