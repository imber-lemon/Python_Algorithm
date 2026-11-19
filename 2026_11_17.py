def tripl(num):
    res = ''
    while num > 2:
        res += str(num % 3)
        num //= 3
    res += str(num)
    return res[::-1]

#
# def make_r(n):
#     r = tripl(n)
#     r += str(n % 3)
#     return int(r, 3)
#
# lst = []
# for n in range(10000):
#     r = make_r(n)
#     if len(str(r)) == 4:
#         lst.append(r)
# print(min(lst))

# n = tripl(9 ** 8 * 3 ** 20 - 3 ** 10 - 3)
# print(str(n).count('2'))


# def f(n):
#     if n == 1:
#         return 1
#     elif n > 1 and n % 2 != 0:
#         return n + f(n-2)
#     elif n % 2 == 0:
#         return n * f(n-1)
# print(f(60))



# def f(a, b, m):
#     if a + b >= 59: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(a + 1, b, m - 1), f(a * 2, b, m - 1), f(a, b + 1, m - 1), f(a, b * 2, m - 1)]
#     return any(h) if m % 2 != 0 else any(h)
# print("19", [s for s in range(1, 54) if f(5, s, 2)])
# print("20", [s for s in range(1, 54) if not f(5, s, 1) and f(5, s, 3)])
# print("21", [s for s in range(1, 54) if not f(5, s, 2) and f(5, s, 4)])




# def fifteen(n):
#     d = {10: 'A',
#          11: 'B',
#          12: 'C',
#          13: 'D',
#          14: 'E'}
#     res = ''
#     while n > 14:
#         ost = n % 15
#         n //= 15
#         if ost <= 9:
#             res += str(ost)
#         else:
#             res += d[ost]
#     if n <= 9:
#         res += str(n)
#     else:
#         res += d[n]
#     return res[::-1]
#
#
# lst = []
# for i in range(10**5):
#     num = fifteen(i)
#     if num.count('8') == 1 and len(num) == 4:
#         for j in range(0, len(num) - 1):
#             if num[j] == num[j+1]:
#                 break
#         lst.append(num)
# print(len(lst))

# N = 1.5 * 2**23
# V = 32000
# r = 16
# Vm = 1.5 * 2**13
#
# V2 = N * V * r // 2**23
# print(V2)
#
# V1 = 25 * 60
# print((V2 - V1) / 1500)