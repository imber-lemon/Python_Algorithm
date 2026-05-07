def letter_comb(digits):
    nums = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    res = []
    matrix = []
    for i in digits:
        matrix.append(nums[i])
    print(matrix)
    if len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 2:
        for i in matrix[0]:
            for x in matrix[1]:
                res.append(i+x)
    elif len(matrix) == 3:
        for i in matrix[0]:
            for j in matrix[1]:
                for x in matrix[2]:
                    res.append(i + j + x)
    elif len(matrix) == 4:
        for i in matrix[0]:
            for j in matrix[1]:
                for x in matrix[2]:
                    for y in matrix[3]:
                        res.append(i + j + x + y)
    return res
#print(letter_comb("23"))

def letter_comb_2(digits):
    nums = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    res = [""]
    for digit in digits:
        new_res = []
        for c in res:
            for letter in nums[digit]:
                new_res.append(c + letter)
                print(new_res, res)
                input()
        res = new_res
    return res
print(letter_comb_2("23"))