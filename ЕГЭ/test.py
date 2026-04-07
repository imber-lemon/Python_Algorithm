def into_base(num, base):
    res = ""
    while num > 1:
        res += str(num % base)
        num //= base
    res += "1"
    return int(res[::-1])


def out_of_base(num, sys):
    base = 1
    res = 0
    for i in range(len(num) - 1, -1, -1):
        res += int(num[i]) * base
        base *= sys
    return res


