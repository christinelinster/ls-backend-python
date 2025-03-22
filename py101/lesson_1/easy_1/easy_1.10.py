# Multiples of 3 and 5 

def multisum(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print(multisum(3))
print(multisum(5))
print(multisum(10))
print(multisum(1000))