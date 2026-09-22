from quick_sort import quick_sort

def binar_search(lst, num):
    lst = quick_sort(lst)
    print("lst:", lst)
    i = len(lst) // 2
    while lst[i] != num:
        if lst[i] > num:
            lst = lst[0:i]
            i = len(lst) // 2
            print(lst, i)
        else:
            lst = lst[i:-1]
            i = len(lst) // 2
            print(lst, i)
print(binar_search([3, 34, 45, 1, 24, 76, 5, 79], 3))
