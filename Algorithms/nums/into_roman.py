def into_roman(n):
    res = ""
    nums = {
        "M" : 1000,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "X" : 10,
        "V" : 5,
        "I" : 1
    }
    for i in n:
        num = ""
        while n >= nums[i]:
            n -= nums[i]
            num += i
            if len(num) >= 4 and i != "M":

        res += num
    return res
print(into_roman(10))