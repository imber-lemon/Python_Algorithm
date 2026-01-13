def subq(words, groups):
    ind = dict()
    for i in range(0, len(words)):
        ind[words[i]] = groups[i]
    res = [str(words[0])]
    c = ind[words[0]]
    for i in ind:
        if ind[i] != c:
            res.append(i)
            c = ind[i]
    return res
print(subq(["e","a","b"],[0,0,1]))