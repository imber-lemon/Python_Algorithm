def lst_move(lst, length, is_right):
    if is_right:
        for i in range(length):
            lst.insert(0, lst[-1])
            lst.pop(-1)
    else:
        for i in range(length):
            lst.append(lst[0])
            lst.pop(0)
    return lst
lst = [1, 2, 3, 4, 5]
lst_move(lst, 2, True)
lst_move(lst, 2, False)
print(lst)