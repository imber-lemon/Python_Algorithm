def is_valid(s):
    lst = ["(", ")", "[", "]", "{", "}"]
    s_new = []
    for i in range(0, len(s)):
        if s[i] in lst:
            s_new.append(lst.index(s[i]))
    for i in range(1, len(s_new)):
        if s_new[i-1] > s_new[i]:
    return True
print(is_valid("[()]"))