# def return_x():
#     for x in range(0, 19):
#         u = (3 + x * 19 + 10 * 19 ** 2 + 1 * 19 ** 3 + 1 * 19 ** 4) + (5 + 4 * 19 + 3 * 19 ** 2 + x * 19 ** 3 + 2 * 19 ** 4 + 1 * 19 ** 5)
#         if u % 14 == 0:
#             return u // 14
# print(return_x())


# def f(n):
#     if n > 1 and n % 6 == 0:
#         return n + f(n // 6 - 2)
#     elif n <= 1:
#         return 0
#     else:
#         return n + f(n + 6)
# print(f(4242))

f = [0] * 4230
for n in range(-5, 4242):
    if n <= 1:
        f[n] = 0
    elif n > 1 and n % 6 == 0:
        f[n] = n + f[n//6-2]
    else:
        f[n] = n + f[n+6]
print(f[4242+5])
