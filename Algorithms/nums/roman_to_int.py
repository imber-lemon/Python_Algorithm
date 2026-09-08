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
    res = ""
    for i in s:
        res