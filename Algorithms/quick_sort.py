import random
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        q = random.choice(lst)
        lower = [elem for elem in lst if elem < q]
        pivot = [q] * lst.count(q)
        higher = [elem for elem in lst if elem > q]
        return quicksort(lower) + pivot + quicksort(higher)

print(quicksort([5, 3, 7, 2, 4]))