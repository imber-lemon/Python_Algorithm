from prime_num import is_prime_num

def factors(num):
    f = []
    for i in range(num // 2 + 1, 1, -1):
        if is_prime_num(i) and num % i == 0:
            f.append(i)
            num = num // i
        if is_prime_num(num):
            f.append(num), f.append(1)
            return f
        elif num == 1:
            f.append(1)
            return f
def factors2(num):
    i = 2
    factors_lst = []
    while num > 1:
        if num % i == 0:
            while num % i == 0:
                num = num // i
                factors_lst.append(i)
        else:
            num += 1
