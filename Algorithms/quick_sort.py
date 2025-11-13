def q_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = lst[len(lst)//2]
        lower = [elem for elem in lst if elem < q]
        pivot = [q] * lst.count(q)
        higher = [elem for elem in lst if elem > q]
        return q_sort(lower) + pivot + q_sort(higher)

print(q_sort([5, 3, 7, 2, 4]))