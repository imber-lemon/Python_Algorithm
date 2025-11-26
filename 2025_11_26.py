def into_base(num, base):
    res = ''
    while num > 1:
        res += str(num % base)
        num //= base
    res += '1'
    return res[::-1]

def find_x():
    for x in range(1000000, 0, -1):
        ur = str(into_base(25 ** 340 + 25 ** 79 - 5 ** 60 + x, 25))
        zeros = ur.count('0')
        if zeros == 287:
            return x
print(find_x())