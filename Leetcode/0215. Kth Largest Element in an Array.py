def find_kth_element(nums, k):
    max_nums = 0
    n = 0
    while n < k:
        max_nums = max(nums)
        nums.remove(max_nums)
        n += 1
    return max_nums
print(find_kth_element([3,2,1,5,6,4], 2))
