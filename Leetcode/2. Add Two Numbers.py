l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
lst = []
s = 0
num1 = 0
num2 = 0
for i in range(0, len(l1)):
    num1 += l1[i] * 10 ** s
    s += 1
s = 0
for i in range(0, len(l2)):
    num2 += l2[i] * 10 ** s
    s += 1
num = num1 + num2
num = str(num)
for i in range(len(num)-1, -1, -1):
    lst.append(int(num[i]))
print(lst)