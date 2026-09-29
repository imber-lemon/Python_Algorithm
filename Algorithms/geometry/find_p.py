def find_p():
    c = 1
    for i in range(3, 10000000, 4):
        c -= 1 / i
    for i in range(5, 10000000, 4):
        c += 1 / i
    return 4 * c
print(find_p())
