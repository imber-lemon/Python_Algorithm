from quick_sort import quick_sort

def binar_search(lst, num):
    lst = quick_sort(lst)
    print("lst:", lst)
    i = len(lst) // 2
    while len(lst) > 1:
        #print(lst[i])
        if lst[i] == num:
            return True
        if lst[i] > num:
            lst = lst[0:i]
            i = len(lst) // 2
            #print(lst, lst[i])
        else:
            lst = lst[i::]
            i = len(lst) // 2
            #print(lst, lst[i])
    return False
print(binar_search([3, 34, 45, 1, 24, 76, 5, 79, 44], 79))
