def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = lst[len(lst)//2]
        lower = [elem for elem in lst if elem < q]
        pivot = [q] * lst.count(q)
        higher = [elem for elem in lst if elem > q]
        return quick_sort(lower) + pivot + quick_sort(higher)
#print(quick_sort([5, 3, 7, 2, 4]))