def third_largest(lst):
    max1 = float("-inf")
    max2 = float("-inf")
    max3 = float("-inf")
    for i in range(len(lst)):
        if lst[i] > max1:
            max1, max2, max3 = lst[i], max1, max2
        elif (lst[i] > max2) and (lst[i] < max1):
            max2, max3 = lst[i], max2
        elif (lst[i] > max3) and (lst[i] < max2):
            max3 = lst[i]
        print(max1, max2, max3)
    return max3
print(third_largest([4, 7, 2, 6, 9, 10, 11]))
