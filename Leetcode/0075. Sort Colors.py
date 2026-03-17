def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    colors = [0, 0, 0]
    for i in nums:
        colors[i] += 1
    nums = [0] * colors[0] + [1] * colors[1] + [2] * colors[2]
    print(nums)
sortColors([2, 0, 2, 1, 1, 0])