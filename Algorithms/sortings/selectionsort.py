def selectionsort(lst):
    max = 0
    lst_new = []
    for i in range(len(lst)):
        for x in range(len(lst)):
            if lst[x] > max:
                max = lst[x]
        lst_new.append(max)
        lst.pop(lst.index(max))
    return lst_new
print(selectionsort([2, 1, 4, 3, 5, 10]))