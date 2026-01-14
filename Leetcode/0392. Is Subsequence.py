def is_subseq(s, t):
    if s:
        t = list(t)
        s = list(s)
        s_ind = 0
        for i in t:
            if i == s[s_ind]:
                s_ind += 1
                if s_ind == len(s):
                    return True
        return False
    else:
        return True
print(is_subseq("abc", "ahbgdc"))