def counting_sort(lst):
    more_than_zero = [0] * (max(lst) + 1)
    less_than_zero = [0] * (-min(lst) + 1)
    for i in range(0, len(lst)):
        if lst[i] >= 0:
            more_than_zero[lst[i]] += 1
        else:
            less_than_zero[-lst[i]] += 1
    lst2 = []
    for i in range(len(less_than_zero)-1, -1, -1):
        for x in range(less_than_zero[i]):
            lst2.append(-i)
    for i in range(0, len(more_than_zero)):
        for x in range(more_than_zero[i]):
            lst2.append(i)
    return lst2
print(counting_sort([1, -1, 2, 10, -6, -4, 11]))
