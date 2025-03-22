# Sum or Product of Consecutive Integers

integer = int(input('Please enter an integer greater than 0: '))
type = input('Enter "s" to compute the sum, or "p" to compute the product: ')

if type == 's'.casefold():
    sum = 0
    for i in range(1, integer + 1):
        sum += i
    print(f'The sum of the integers between 1 and {integer} is {sum}')
elif type == 'p'.casefold():
    product = 1
    for i in range(1, integer + 1):
        product *= i
    print(f'The product of the integers between 1 and {integer} is {product}')
else:
    print('Oops. Unknown operation')