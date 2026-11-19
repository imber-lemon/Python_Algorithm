import sys
from sys import setrecursionlimit

sys.setrecursionlimit(10**8)

# def make_r(n):
#     r = oct(n)[2:]
#     if n % 7 == 0:
#         r += r[-2::]
#     else:
#         r = oct((int(n) % 7) * 7)[2:] + r
#     return int(r)
#
# lst = []
# nums = []
# for i in range(20, 100000):
#     r = make_r(i)
#     if r > 500:
#         lst.append(r)
#         nums.append(i)
# print(min(lst), nums[lst.index(min(lst))])




# num = 4 ** 14 + 2 ** 32 - 4
# bin_num = bin(num)[2:]
# print(bin_num.count('1'))

# count = 1
# lst = ["а", "и", "о", "у", "э"]
# for i in range(5):
#     for j in range(5):
#         for h in range(5):
#             for k in range(5):
#                 w = lst[i] + lst[j] + lst[h] + lst[k]
#                 if w == "иааэ":
#                     print(count)
#                 count += 1

#
# def f(n):
#     if n == 1:
#         return 1
#     else:
#         return f(n-1)*(n+1)
# print(f(4))


def f(a, m):
    if a > 31: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 1, m - 1), f(a * 3 + 1, m - 1)]
    return any(h) if m % 2 != 0 else all(h)
print("19", [s for s in range(1, 32) if f(s, 2)])
print("20", [s for s in range(1, 32) if not f(s, 1) and f(s, 3)])
print("19", [s for s in range(1, 32) if not f(s, 2) and f(s, 4)])