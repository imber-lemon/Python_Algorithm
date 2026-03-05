def find_kth_element(nums, k):
    lst = [0] * (max(nums) - min(nums) + 1)
    for i in nums:
        lst[abs(i)-1] += 1
    x = len(lst) - 1
    while k > 0:
        if lst[x] >= 1:
            if lst[x] > k:
                print(x)
                if x + 1 not in nums:
                    return -(x + 1)
                else:
                    return x + 1
            else:
                k -= lst[x]
                if k == 0:
                    if x + 1 not in nums:
                        return -(x + 1)
                    else:
                        return x + 1
        x -= 1
    if x not in nums:
        return -x
    else:
        return x
print(find_kth_element([99, 99], 2))