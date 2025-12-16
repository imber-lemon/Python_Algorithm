eq = '3+5*10/2'
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
print(n)
print(s)

i = 0
while '*' in s and '/' in s:
    if s[i] == '*':
        n[i] = int(n[i]) * int(n[i+1])
        n.pop(i + 1)
        s.pop(i)
        print(n)
    elif s[i] == '/':
        n[i] = int(n[i]) // int(n[i+1])
        n.pop(i + 1)
        s.pop(i)
    i += 1
print(n)
print(s)
for i in range(0, len(s)):
    if s[i] == '+' and len(n) > 2:
        n[i] = int(n[i]) + int(n[i+1])
        n.pop(i + 1)
        print(n, s)
    elif s[i] == '-' and len(n) > 2:
        n[i] += int(n[i]) - int(n[i+1])
        n.pop(i + 1)
        print(n, s)

    if s[i] == '+' and len(n) <= 2:
        res += int(n[0]) + int(n[1])
    elif s[i] == '-' and len(n) <= 2:
        res += int(n[0]) - int(n[1])
print(res)