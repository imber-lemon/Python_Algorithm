def cut_lst(lst):
    if len(lst) < 2:
        return lst
    else:
        p = len(lst)//2
        higher = lst[0:p]
        lower = lst[p:len(lst)]
        return cut_lst(higher), cut_lst(lower)


# def merge_sort(lst_new, lst):
#     last_lst = [0] * len(lst)
#     for i in range(1, len(lst_new)):
#         if lst[i]
lst = [5 ,3, 7, 2, 9]
lst_new = cut_lst(lst)
print(lst_new)
