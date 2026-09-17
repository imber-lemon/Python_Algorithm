def counting_sort(lst):
    more_than_zero = [0] * max(lst)
    less_than_zero = [0] * (-min(lst) + 1)
    for i in range(0, len(lst)):
        if lst[i] >= 0:
            more_than_zero[lst[i]] += 1
        else:
            less_than_zero[-lst[i]] += 1
    print(less_than_zero)
    print(more_than_zero)
print(counting_sort([1, -1, 2, 10, -6, -4, 11]))
