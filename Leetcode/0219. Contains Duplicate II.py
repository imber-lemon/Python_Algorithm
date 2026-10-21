def cont_dubl_2(nums, k):
    d = dict()
    for i in range(len(nums)):
        if nums[i] in d:
            if abs(d[nums[i]] - i) <= k:
                return True
        d[nums[i]] = i
    return False
print(cont_dubl2([1, 2, 3, 1, 2, 3], 2))
