def sum_of_nums_uni(n):
    res = 0
    while n >= 1:
        res += n % 10
        n //= 10
    return res


def sum_of_nums_python(n):
    n = str(n)
    res = 0
    for i in n:
        res += int(i)
    return res


print(sum_of_nums_uni(2312412))
