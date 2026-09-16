def bubblesort(lst):
    for i in range(len(lst)):
        for x in range(len(lst) - 1):
            if lst[x] > lst[x + 1]:
                lst[x], lst[x + 1] = lst[x + 1], lst[x]
lst = [2, 1, 3, 5, 4, 7]
bubblesort(lst)
print(lst)