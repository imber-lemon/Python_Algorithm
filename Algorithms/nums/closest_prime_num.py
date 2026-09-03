from prime_num import is_prime_num

def closest_pr_num(num):
    j = num + 1
    num1 = 0
    num2 = 0
    for i in range(num - 1, 0, -1):
        if is_prime_num(i):
            num1 = i
            break
    while True:
        if is_prime_num(j):
            num2 = j
            break
        else:
            j += 1
    if (num2 - num) > (num - num1):
        return num1
    else:
        return num2
print(closest_pr_num(1))