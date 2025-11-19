def isomorphic_str(s, t):
    alp = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z')
    ind_t = [0] * 26
    ind_s = [0] * 26
    if len(s) != len(t):
        return False
    else:
        for i in range(0, len(s)):
            ind_t[alp.index(t[i])] += 1
            ind_s[alp.index(s[i])] += 1
        for j in range(0, len(ind_t)):
            if ind_t[j] == 0:
                ind_t.pop(j)
        print(ind_s)
        print(ind_t)
print(isomorphic_str('add', 'egg'))
