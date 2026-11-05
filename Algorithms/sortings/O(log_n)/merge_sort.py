def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    return merge(merge_sort(lst[0:len(lst)//2]), merge_sort(lst[len(lst)//2:]))

def merge(left, right):
    sorted_lst = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_lst.append(right[j])
            j += 1
        else:
            sorted_lst.append(left[i])
            i += 1

    if i == len(left):
        for k in range(j, len(right)):
            sorted_lst.append(right[k])
    else:
        for k in range(i, len(left)):
            sorted_lst.append(left[k])

    return sorted_lst


lst = [5, 3, 6, 2, 1, 9, 10]
# 1 2 3 5 6 9 10
print(merge_sort(lst))

