def reverse_vowels(s):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    lst = []
    s_lst = [0] * len(s)
    for i in range(0, len(s)):
        s_lst[i] = s[i]
    for i in s:
        if i in v:
            lst.append(i)
    for i in range(0, len(s_lst)):
        if s_lst[i] in v:
            s_lst[i] = lst[-1]
            lst.pop(-1)
    s_new = ''
    for i in range(0, len(s_lst)):
        s_new += s_lst[i]
    return s_new
print(reverse_vowels('leetcode'))