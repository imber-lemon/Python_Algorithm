def search_in_rt_arr(nums, target):
    i = 0
    while nums[i] != target:
        i += 1
        if i == len(nums):
            return -1
    return i
print(search_in_rt_arr([1], 0))