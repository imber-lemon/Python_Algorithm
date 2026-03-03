def find_kth_element(nums, k):
    min_lst = min(nums)
    lst = [0] * max(nums)
    for i in nums:
        lst[i-1] += 1
    for i in range(len(lst) - 1, -1, -1):
        if k > lst[i]:
            k -= lst[i]
        else:
            return i
        if k == 0:
            return i
print(find_kth_element([3,2,3,1,2,4,5,5,6], 4))