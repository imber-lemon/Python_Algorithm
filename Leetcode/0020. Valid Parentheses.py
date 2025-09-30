def is_valid(s):
    lst = ["(", ")", "[", "]", "{", "}"]
    s_new = []
    for i in range(0, len(s)):
        if s[i] in lst:
            s_new.append(lst.index(s[i]))
    print(s_new)
    j = 0
    for k in range(len(s_new) - 1, len(s_new)//2, - 1):
        if s_new[j] != s_new[k] - 1:
            return False
        else:
            j += 1
    for i in range(1, len(s_new), 2):
        if s_new[i-1] > s_new[i]:
            return False
        elif s_new[i-1] + 1 != s_new[i]:
            return False
    return True
print(is_valid("{[]}"))
