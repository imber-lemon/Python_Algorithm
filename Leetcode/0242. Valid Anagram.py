def is_anagram(s, t):
    col_s = set()
    col_t = set()
    for i in s:
        col_s.add(i)
    for i in t:
        col_t.add(i)
    if col_t == col_s:
        return True
    else:
        return False
print(is_anagram('anagram', 'nagaram'))
