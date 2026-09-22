def selectionsort(lst):
    min_num = 9999999
    lst_new = []
    for i in range(len(lst)):
        for x in range(len(lst)):
            if lst[x] < min_num:
                min_num = lst[x]
        lst_new.append(min_num)
        #lst.pop(lst.index(max))
        lst.remove(min_num)
        min_num = 99999999
    return lst_new
print(selectionsort([2, 1, 4, 3, 5, 10]))
