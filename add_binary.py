def add_binary():
    a = 11
    b = 1
    integer_sum= int(a, 2) + int(b, 2)
    binary_sum = bin(integer_sum)
    print(binary_sum[2:])