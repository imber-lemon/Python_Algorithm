# def F(n):
#     if n == 1:
#         return 2
#     elif n > 1 and F(n - 1) < 7555444:
#         return F(n - 1) + 6
#     else:
#         return F(n - 1) - 7555444
#
#
#


f = [0] * 7555451
for n in range(0, 7555451):
    if n == 1:
        f[n] = 2
    elif n > 1 and f[n - 1] < 7555444:
        f[n] = f[n - 1] + 6
    else:
        f[n] = f[n - 1] - 7555444

print(f[7555450])

