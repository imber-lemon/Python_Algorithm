def into_base(num, base):
    res = ""
    while num > 1:
        res += str(num % base)
        num //= base
    res += "1"
    return res[::-1]


def find_x():
    for x in range(2070, 0, -1):
        task = into_base(7 ** 230 + 7 ** 130 + 7 ** 30 - x, 7)
        task = str(task)
        zeros = task.count('0')
        if zeros == 199:
            return x
print(find_x())