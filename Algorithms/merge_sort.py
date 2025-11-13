# def cut_lst(lst):
#     if len(lst) < 2:
#         return lst
#     else:
#         p = len(lst)//2
#         higher = lst[0:p]
#         lower = lst[p:len(lst)]
#         return cut_lst(higher), cut_lst(lower)

def merge(lst):
    n = 2
    lst_new = [0] * (len(lst) // n)
    for i in range(0, len(lst) - n, n):
        lst_new[i] = lst[i:i+n]
    n *= 2
    return lst_new
lst = [[5] ,[3], [7], [2], [9], [6]]
print(merge(lst))
