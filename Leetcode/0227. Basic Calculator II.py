eq = '3+5*10'
s_ind = []
s = []
n = []
nums = '0123456789'
for i in range(len(eq)):
    if eq[i] not in nums:
        s.append(eq[i])
        s_ind.append(i)
i_last = 0
for i in s_ind:
    n.append(eq[i_last:i])
    i_last = i + 1
n.append(eq[i_last:len(eq)])
res = 0
for i in range(0, len(s)):
    if s[i] == '*':
        n[i] = int(n[i]) * int(n[i+1])
        n.pop(i+1)
        s.pop(i)
    elif s[i] == '/':
        n[i] = int(n[i]) // int(n[i+1])
        n.pop(i+1)
        s.pop(i)
    if '*' and '/' not in s:
        print(n)
        print(s)
        for i in range(0, len(s)):
            if s[i] == '+':
                res += int(n[i]) + int(n[i+1])
                print(int(n[i]), int(n[i+1]),int(n[i]) + int(n[i+1]))
            elif s[i] == '-':
                res += int(n[i]) - int(n[i+1])

print(res)