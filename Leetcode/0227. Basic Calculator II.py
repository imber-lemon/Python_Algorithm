# def basic_calc(eq):
#     s_ind = []
#     s = []
#     n = []
#     nums = '0123456789'
#     for i in range(len(eq)):
#         if eq[i] not in nums:
#             s.append(eq[i])
#             s_ind.append(i)
#     i_last = 0
#     for i in s_ind:
#         n.append(eq[i_last:i])
#         i_last = i + 1
#     n.append(eq[i_last:len(eq)])
#     res = 0
#
#     i = 0
#     while ('*' in s) or ('/' in s) and s:
#         if len(n) > 1:
#             if len(s) <= i:
#                 break
#             elif s[i] == '*':
#                 print(s[i])
#                 n[i] = int(n[i]) * int(n[i+1])
#                 n.pop(i + 1)
#                 s.pop(i)
#                 print(n, s)
#                 input()
#             print(i)
#             if s[i] == '/':
#                 # print(s[i])
#                 n[i] = int(n[i]) // int(n[i+1])
#                 n.pop(i + 1)
#                 s.pop(i)
#                 print(n, s)
#                 input()
#                 i -= 1
#             i += 1
#             if len(n) == 1:
#                 return n[0]
#
#     print(n)
#     print(s)
#     i = 0
#     while len(n) > 1:
#         if s[i] == '+':
#             n[i] = int(n[i]) + int(n[i+1])
#             n.pop(i + 1)
#             s.pop(i)
#             # print(n, s)
#         elif s[i] == '-':
#             n[i] += int(n[i]) - int(n[i+1])
#             n.pop(i + 1)
#             s.pop(i)
#             # print(n, s)
#         i += 1
#     return n[0]
# print(basic_calc('6+2*4'))
symb = '+-/*'
eq = '6+2+4'
last_n = 0
res = 0
s = 0
n = 0
eq = list(eq)
for i in range(len(eq)):
    if eq[i] in symb:
        if eq[i] == '+':
            n = int(eq[i-1]) + int(eq[i+1])
            res += n
            eq[i+1] = n
            print(res)
        elif eq[i] == '-':
            n = int(eq[i - 1]) - int(eq[i + 1])
            res += n
            eq[i+1] = n
            print(res)
        elif eq[i] == '*':
            n = int(eq[i - 1]) * int(eq[i + 1])
            res += n
            eq[i+1] = n
            print(res)
        else:
            n = int(eq[i - 1]) // int(eq[i + 1])
            res += n
            eq[i+1] = n
            print(res)
    # else:
    #     if '/' in eq and '*' in eq:
    #         if s == '*':
    #             res += last_n * n
    #             last_n = last_n * n
    #             print(last_n, s, n, res)
    #         elif s == '/':
    #             res += last_n // n
    #             last_n = last_n // n
    #             print(last_n, s, n, res)
    #     else:
    #         if s == '+':
    #             res += last_n + n
    #             last_n = last_n + n
    #             print(last_n, s, n, res)
    #         else:
    #             res += last_n - n
    #             last_n = last_n - n
    #             print(last_n, s, n, res)
    #     n = int(i)
print('  ', res)