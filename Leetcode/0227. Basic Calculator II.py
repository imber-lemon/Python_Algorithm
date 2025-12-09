eq = '3+5*10'
s = []
s_ind = []
n = []
nums = '0123456789'
for i in range(len(eq)):
    if eq[i] not in nums:
        s.append(eq[i])
        s_ind.append(i)
    # else:
    #     x = 0
    #     while eq[x] in nums:
    #         num += eq[x]
    #         x += 1
    #     n.append(num)
    #     num = ''
i_last = 0
for i in s_ind:
    n.append(eq[i_last:i])
    i_last = i + 1
n.append(eq[i_last:len(eq)])
print(n)
print(s)
