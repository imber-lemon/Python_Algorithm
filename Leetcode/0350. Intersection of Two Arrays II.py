def intersect(nums1, nums2):
    res = []
    i = 0
    while i < len(nums1):
        if nums1[i] in nums2:
            res.append(nums1[i])
            nums2.pop(nums2.index(nums1[i]))
        i += 1
    return res
print(intersect([1, 2, 2, 1], [2]))