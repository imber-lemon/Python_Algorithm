# def threeSum(nums):
#     lst = []
#     been = []
#     for i in range(len(nums)-2):
#         for j in range(len(nums)-1):
#             for k in range(len(nums)):
#                 if i != j and j != k and i != k and nums[i] + nums[j] + nums[k] == 0 and {nums[i], nums[j],nums[k]} not in been:
#                     lst.append([nums[i], nums[j], nums[k]])
#                     been.append({nums[i], nums[j], nums[k]})
#     return lst
# print(threeSum([0, 1, 1]))
def threeSum(nums):
    nums.sort()
    lst = []
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0 and [nums[i], nums[j], nums[k]] not in lst:
                lst.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif sum < 0:
                j += 1
            else:
                k -= 1
    return lst
print(threeSum([-1, 0, 1, 2, -1, -4]))
