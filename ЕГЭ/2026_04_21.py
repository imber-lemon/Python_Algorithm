# import sys
#
# sys.setrecursionlimit(10**6)
#
# def f(n):
#     if n >= 21:
#         return f(n - 8) + 1095
#     else:
#         return 10 * (G(n - 7) - 36)
# def G(n):
#     if n >= 22560:
#         return n / 23 + 33
#     else:
#         return G(n + 11) - 4
# print(f(548))

f = [0] * 10000
g = [0] * 100000
for n in range(22600, -1, -1):
    if n < 22560:
        g[n] = g[n + 11] - 4
    else:
        g[n] = n / 23 + 33
for n in range(0, 550):
    if n < 21:
        f[n] = 10 * (g[n-7] - 36)
    else:
        f[n] = f[n-8] + 1095
print(f[548])
