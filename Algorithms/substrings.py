def substrings(s1, s2):
    #s1 - подстрока
    #s2 - строка
    c = 0
    i = 0
    while i < len(s2):
        if s2[i] == s1[0] and s2[i] != " ":
            #print(i, s2[i], s2[i:i+len(s1)])
            if s2[i:i+len(s1)] == s1:
                c += 1
                i += len(s1) - 1
        i += 1
    return c
print(substrings("aa", "aaaaa"))
