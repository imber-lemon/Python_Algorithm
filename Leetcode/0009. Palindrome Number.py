x = 12121
x2 = ""
n = 0
x = str(x)
for i in range(len(x)-1, -1, -1):
    x2 += x[i]
print(x, x2)
print(x == x2)
