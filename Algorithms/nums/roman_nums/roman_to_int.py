def roman_to_int(s):
    nums = {
        "M" : 1000,
        "D" : 500,
        "C" : 100,
        "L" : 50,
        "X" : 10,
        "V" : 5,
        "I" : 1
    }
    res = 0
    while i
        if nums[s[i]] > nums[s[i + 1]]:
            res += nums[s[i]]
        else:
            res += nums[s[i + 1]] - nums[s[i]]
            i += 1
    return res
print(roman_to_int("VI"))