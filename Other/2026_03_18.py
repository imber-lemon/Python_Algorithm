# def n_to_zero(n):
#     if n != 0:
#         print(n)
#         return n_to_zero(n - 1)
#     else:
#         return 0
# print(n_to_zero(10))

# def sum_from_n_to_zero(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_from_n_to_zero(n - 1)
# print(sum_from_n_to_zero(9))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))