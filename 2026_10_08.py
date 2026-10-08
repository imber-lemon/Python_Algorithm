from itertools import product

c = 0
for i in product([0, 1, 2, 3, 4, 5, 6, 7], repeat = 5):
    if i[0] != 0:
        if i.count(6) == 1:
            ind = i.index(6)
            if ind == len(i) - 1 and i[abs(ind - 1)] % 2 == 0:
                c += 1
            elif ind == 0 and i[ind + 1] % 2 == 0:
                c += 1
            elif ind > 0 and ind < (len(i) - 1) and i[ind + 1] % 2 == 0 and i[ind - 1] % 2 == 0:
                c += 1
print(c)