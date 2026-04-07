# f1 = 1
# f2 = 3
# f3 = f2 * 3 + f1 * 2
# f4 = f3 * 4 + f2 * 3
# f5 = f4 * 5 + f3 * 4
# print(f5)

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return f(n - 1) * n + f(n - 2) * (n - 1)
print(f(5))