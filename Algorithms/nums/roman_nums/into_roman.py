# def into_roman(n):
#     res = ""
#     nums = {
#         "M" : 1000,
#         "D" : 500,
#         "C" : 100,
#         "L" : 50,
#         "X" : 10,
#         "V" : 5,
#         "I" : 1
#     }
#     for i in n:
#         num = ""
#         while n >= nums[i]:
#             n -= nums[i]
#             num += i
#             if len(num) >= 4 and i != "M":
#
#         res += num
#     return res


def into_roman(n):
    M = ["", "M", "MM", "MMM", "MMMM", "MMMMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    res = ""
    if n >= 1000:
        res += M[n // 1000]
        n = n % 1000
    if n >= 100:
        res += C[n // 100]
        n = n % 100
    if n >= 10:
        res += X[n // 10]
        n = n % 10
    if n >= 1:
        res += I[n]
    return res
print(into_roman(1500))
