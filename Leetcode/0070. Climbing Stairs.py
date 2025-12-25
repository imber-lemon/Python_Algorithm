# def steps(n):
#     lst = []
#     for i in range(0, n):
#         for x in range(0, n):
#             if x + i == n:
#                 lst.append(f'{x} + {i}')
#     if '1 + '* (n-1) + '1' not in lst:
#         lst.append('1 + '* (n-1) + '1')
#     return len(lst), lst
# print(steps(4))


n = 4
lst = [i for i in range(1, n+1)]
print(lst)
