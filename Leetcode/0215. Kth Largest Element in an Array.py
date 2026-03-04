def find_kth_element(nums, k):
    lst = [0] * abs(max(nums))
    for i in nums:
        lst[abs(i)-1] += 1
    x = len(lst) - 1
    while k > 0:
        if lst[x] >= 1:
            if lst[x] > k:
                return x + 1
            else:
                k -= lst[x]
                if k == 0:
                    return x + 1
        x -= 1
    return x
print(find_kth_element([-1, -1], 2))