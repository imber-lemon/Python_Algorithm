# def fib(n):
#     n0 = 1
#     n1 = 1
#     res = "1 1 "
#     for i in range(n-2):
#         res += str(n0 + n1)
#         n2 = n1 + n0
#         n0 = n1
#         n1 = n2
#         res += " "
#     return res
# print(fib(5))

def fib(n):
    n0 = 1
    n1 = 1
    for i in range(n-2):
        n0, n1 = n1, n0 + n1
    return n0
print(fib(6))


