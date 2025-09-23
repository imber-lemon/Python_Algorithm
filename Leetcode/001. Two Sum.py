nums = [2, 7, 11, 15]
target = 9
lst2 = []
s = 1
for i in range(0, len(nums)):
    for x in range(s, len(nums)):
        if nums[i] + nums[x] == target:
            lst2.append(i), lst2.append(x)
    s += 1
print(lst2)
