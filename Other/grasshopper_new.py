from random import randint
lst = [0] * 20
for i in range(0, len(lst)):
    lst[i] = randint(0, 20)
print(lst)
sum = 0
i = -1
while i != len(lst):
    num = min(lst[i+1], lst[i+2])
    sum += num
    i = lst.index(num)
    print(i)
print(sum)
