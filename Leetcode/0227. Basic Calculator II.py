def basic_calc(eq):
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

    i = 0
    while ('*' in s) or ('/' in s) and s:
        if len(n) > 1:
            if len(s) <= i:
                break
            elif s[i] == '*':
                print(s[i])
                n[i] = int(n[i]) * int(n[i+1])
                n.pop(i + 1)
                s.pop(i)
                print(n, s)
                input()
            print(i)
            if s[i] == '/':
                # print(s[i])
                n[i] = int(n[i]) // int(n[i+1])
                n.pop(i + 1)
                s.pop(i)
                print(n, s)
                input()
                i -= 1
            i += 1
        else:
            return n[0]

    print(n)
    print(s)
    i = 0
    while len(n) > 1:
        if s[i] == '+':
            n[i] = int(n[i]) + int(n[i+1])
            n.pop(i + 1)
            s.pop(i)
            # print(n, s)
        elif s[i] == '-':
            n[i] += int(n[i]) - int(n[i+1])
            n.pop(i + 1)
            s.pop(i)
            # print(n, s)        
        i += 1
    return n[0]
print(basic_calc('3/2*2'))




eq = '3+4/2'
symb = '+-*/'
last_n = 0
res = 0
for i in range(0, len(eq)):
    if eq[i] not in symb:
        last_n = int(eq[i])
        print(last_n)
        eq.replace(eq[i], "")
    else:
        if eq[i] == '+':
            num = (last_n + int(eq[i+1]))
            res += num
            last_n = num
            print(last_n, eq[i], eq[i + 1])
        elif eq[i] == '-':
            num = (last_n - int(eq[i+1]))
            res += num
            last_n = num
            print(last_n, eq[i], eq[i + 1])
        elif eq[i] == '*':
            num = (last_n * int(eq[i+1]))
            res += num
            last_n = num
            print(last_n, eq[i], eq[i + 1])
        elif eq[i] == '/':
            num = (last_n // int(eq[i+1]))
            res += num
            last_n = num
            print(last_n, eq[i], eq[i + 1])
print(res)
