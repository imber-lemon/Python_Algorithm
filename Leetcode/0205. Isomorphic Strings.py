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
        j = 0
        while j != len(ind_t):
            if ind_t[j] == 0:
                ind_t.pop(j)
                j -= 1
            j += 1
        x = 0
        while x != len(ind_s):
            if ind_s[x] == 0:
                ind_s.pop(x)
                x -= 1
            x += 1
        if ind_s == ind_t:
            return True
        else:
            ind_s.sort()
            ind_t.sort()
            if ind_t == ind_s:
                return True
            else:
                return False
print(isomorphic_str('bbbaaaba', 'aaabbbba'))
