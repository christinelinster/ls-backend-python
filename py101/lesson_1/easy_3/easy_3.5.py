# Right Triangles

def triangle(n):
    for i in range(1, n + 1):
        print(f'{' ' * (n - i)}{'*' * i}')

triangle(9)