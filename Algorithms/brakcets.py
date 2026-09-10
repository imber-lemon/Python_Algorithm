# def are_brackets_ok(s: str):
#     c = 0
#     for i in s:
#         if i == "(":
#             c += 1
#         elif i == ")":
#             c -= 1
#             if c == -1:
#                 return False
#     if c == 0:
#         return True
#     else:
#         return False
# print(are_brackets_ok("()()"))
from inspect import stack


def are_brackets_ok(string: str):
    o_brac = ["(", "[", "{"]
    c_brac = [")", "]", "}"]
    stack = []
    for i in string:
        if i in o_brac:
            stack.append(i)
        elif i in c_brac:
            if stack[-1].index(o_brac) == i.index(c_brac):
                stack.re
print(are_brackets_ok(""))