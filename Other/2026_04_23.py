lst = [int(i) for i in open('17.txt', encoding='utf-8-sig')]
not_max = []
maxi = 0
while maxi % 100 != 28:
    maxi = max(list(set(lst) - set(not_max)))
    if maxi % 100 != 28:
        not_max.append(maxi)
c = 0
max_sum = 0
for i in range(0, len(lst) - 2):
    if sum(lst[i:i+3]) > 0 and sum(lst[i:i+3]) / 3 < maxi:
        if sum(lst[i:i+3]) > max_sum:
            max_sum = sum(lst[i:i+3])
        for x in lst[i:i+3]:
            if 99 < abs(x) < 1000:
                c += 1
                break
print("всего троек:", c)
print("макс сумма:", max_sum)
