# Easy 2.3

# Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.

print(42 >= 10 and 42 <= 100)
print(100 >= 10 and 100 <= 100)
print(101 >= 10 and 101 <= 100)

print(42 in range(10, 101))
print(100 in range(10, 101))
print(101 in range(10, 101))