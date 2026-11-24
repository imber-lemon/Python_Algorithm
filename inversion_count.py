# def inversion_count(lst):
#     inv = 0
#     for i in range(0, len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 inv += 1
#     return inv
# print(inversion_count([4, 2, 7, 8, 1, 3]))


# # [1, 3, 2, 4]
def inversion_count(lst):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, an_left = merge_sort(arr[:mid])
        right, an_right = merge_sort(arr[mid:])
        merged, an_merged = merge(left, right)

        return merged, an_left + an_right + an_merged

    def merge(left, right):
        inv_count = 0
        lst_return = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                lst_return.append(left[l])
                l += 1
            else:
                lst_return.append(right[r])
                r += 1
                inv_count += len(left) - l


        for i in range(l, len(left)):
            lst_return.append(left[i])

        for k in range(r, len(right)):
            lst_return.append(right[k])

        return lst_return,inv_count

    q, final_num = merge_sort(lst)

    return final_num

print(inversion_count([5, 4, 3, 2, 1]))