def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = lst[len(lst) // 2]
    left = [i for i in lst if i < mid]
    mid_lst = [mid] * lst.count(mid)
    right = [i for i in lst if i > mid]
    return quick_sort(left) + mid_lst + quick_sort(right)

sorted_lst = [5, 5, 2, 1, 9, 10, 4]
print(quick_sort(sorted_lst))