def shortest_word(strs):
    min_len = len(strs[0])
    for i in range(1, len(strs)):
        if min_len > len(strs[i]):
            min_len = len(strs[i])
    return min_len

def longest_common_prefix(strs):
    lcp = ""
    min_len = shortest_word(strs)
    word = strs[0]
    for i in range(0, int(min_len)):
        for x in range(0, len(strs)):
            if word[i] != strs[x][i]:
                return lcp
        lcp += word[i]
    return lcp

print(longest_common_prefix(["flower","flow","flight"]))