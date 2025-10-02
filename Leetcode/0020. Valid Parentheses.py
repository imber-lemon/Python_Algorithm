# def is_valid(s):
#     lst = ["(", ")", "[", "]", "{", "}"]
#     s_new = []
#     for i in range(0, len(s)):
#         if s[i] in lst:
#             s_new.append(lst.index(s[i]))
#     if len(s_new) % 2 == 0:
#         for x in range(0, len(s_new)):
#             for i in range(x, len(s_new), 2):
#                 if (s_new[x] + 1 == s_new[i] or s_new[x]-1 == s_new[i]) and s_new[i] % 2 == 1:
#                     j = 0
#                     for k in range(len(s_new) - 1, len(s_new) // 2 - 1, - 1):
#                         if s_new[j] + 1 != s_new[k]:
#                             return False
#                         j += 1
#         return True
#     else:
#         return False
# print(is_valid("[)"))
#                     print(s_new)
#                     s_new.remove(s_new[i-1])
#                     s_new.remove(s_new[i])
#                     print(s_new)
# print(is_valid("()"))


def is_valid(s):
    lst = ["(", ")", "[", "]", "{", "}"]
    lst_new = []
    s_new = []
    for i in range(0, len(s)):
        if s[i] in lst:
            s_new.append(lst.index(s[i]))
    print(s_new)
    for x in range(0, len(s_new)):
        for i in range(x+1, len(s_new)):
            if s_new[x] + 1 == s_new[i]:
                print(x)
                print(i)
                lst_new.append(x)
                lst_new.append(i)
    for i in range(0, len(lst_new)):
        s_new.pop(lst_new[i])
    print(s_new)
    if len(s_new) == 0:
        return True
    else:
        return False
print(is_valid("[()]"))