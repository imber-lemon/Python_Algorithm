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
    open_br = ["(", "[", "{"]
    close_br = [")", "]", "}"]
    s_new = []
    lst = []
    for j in range(0, len(s)):
        s_new.append(s[j])
    for i in range(0, len(s_new)):
        if s[i] in open_br:
            lst.append(s[i])
        elif s[i] in close_br:
             if open_br.index(lst[len(lst)-1]) == close_br.index(s[i]):
                 lst.remove(len(lst)-1)
    #         for x in range(i-1, -1, -1):
    #             if (s_new[x] in open_br) and (close_br.index(s_new[i]) == open_br.index(s_new[x])):
    #                 s_new.remove(s_new[x])
    #                 s_new.remove(s_new[i])
    # if len(s_new) == 0:
    #     return True
    # else:
    #     return False
    print(lst)
print(is_valid("[[[]"))

