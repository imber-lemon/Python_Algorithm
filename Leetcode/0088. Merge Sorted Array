def merge_lists(nums1, m, nums2, n):
    if m == 0:
        for i in nums2:
            nums1.append(i)
    elif m > 0 and n > 0:
        x = 0
        for i in range(0, m + n):
            print(nums1[i], nums1[i + 1], nums2[x])
            if nums1[i] <= nums2[x] and nums1[i + 1] >= nums2[x]:
                nums1.insert(i + 1, nums2[x])
                x += 1
                print('1', nums1)
            elif nums1[i] <= nums2[x] and nums1[i + 1] == 0:
                while x < n:
                    nums1[x + m] = nums2[x]
                    x += 1
                print('2', nums1)
    else:
        pass
    print(nums1)
print(merge_lists([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
