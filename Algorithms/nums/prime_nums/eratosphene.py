def erato(num):
    lst = [True] * num
    lst[0] = lst[1] = False
    for i in range(2, num):
        if lst[i]:
            for l in range(i, num, i):
                lst[l] = False
    return lst
print(erato(20))
