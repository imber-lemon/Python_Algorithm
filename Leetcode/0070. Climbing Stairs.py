n = 3
lst = []
for i in range(0, n):
    for x in range(0, n):
        if x + i == n:
            lst.append(f'{x} + {i}')
lst.append('1 + '* (n-1) + '1')
res = ''
for i in lst:
    for j in i:
        if j == '1':
            res += '1 step'
        else:
            res += str(j) + ' steps'
print(res)
