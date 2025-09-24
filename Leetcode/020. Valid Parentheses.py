s = "[()]"
lst = ["(", ")", "[", "]", "{", "}"]
s_new = []
for i in range(0, len(s)):
    if s[i] in lst:
        s_new.append(lst.index(s[i]))
print(s_new)
for i in range(0, len(s_new)):
