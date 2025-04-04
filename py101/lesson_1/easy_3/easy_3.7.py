# Double Doubles

# Double Doubles

def twice(n):
    n_str = str(n)
    middle =  len(n_str) // 2
    str_1 = n_str[:middle]
    str_2 = n_str[middle:]

    return n if(str_1 == str_2) else n * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
