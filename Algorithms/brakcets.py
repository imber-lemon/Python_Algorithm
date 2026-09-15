from collections import deque

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



# def are_brackets_fine(string: str):
#     o_brac = ["(", "[", "{"]
#     c_brac = [")", "]", "}"]
#     stack = []
#     for i in string:
#         if i in o_brac:
#             stack.append(i)
#         elif i in c_brac:
#             if stack:
#                 if o_brac.index(stack[-1]) == c_brac.index(i):
#                     stack.pop(-1)
#                 else:
#                     return False
#             else:
#                 return False
#     if len(stack) == 0:
#         return True
#     else:
#         return False
# print(are_brackets_fine("}}{}()[]())"))


def are_brackets_fine(string):
    o_brac = ["(", "[", "{"]
    c_brac = [")", "]", "}"]
    stack = deque([])
    for i in string:
        if i in o_brac:
            stack.append(i)
        elif i in c_brac:
            if stack:
                if o_brac.index(stack[-1]) == c_brac.index(i):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False
print(are_brackets_fine("([]{})"))
