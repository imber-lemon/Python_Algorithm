def sum_of_nums_uni(n):
    c = 10
    res = 0
    while n > c:
        res += n % 10
        n //= 10
        c *= 10
    return res + n // 10 + n % 10
print(sum_of_nums_uni(1354))