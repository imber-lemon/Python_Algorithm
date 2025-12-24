def bas_calc(eq):
    num = 0
    nums = []
    sym = []

    for i in eq:
        if i.isdigit():
            num = num * 10 + int(i)
        else:
            nums.append(num)
            num = 0
            sym.append(i)
    nums.append(num)

    i = 0
    while i < len(sym):
        if sym[i] == '*':
            nums[i] = nums[i] * nums[i+1]
            nums.pop(i+1)
            sym.pop(i)
        elif sym[i] == '/':
            nums[i] = int(nums[i] / nums[i+1])
            nums.pop(i+1)
            sym.pop(i)
        else:
            i += 1

    i = 0
    while i < len(sym):
        if sym[i] == '+':
            nums[i] = nums[i] + nums[i+1]
            nums.pop(i+1)
            sym.pop(i)
        elif sym[i] == '-':
            nums[i] = nums[i] - nums[i+1]
            nums.pop(i+1)
            sym.pop(i)
        else:
            i += 1

    return nums[0]
print(bas_calc('3+2*2'))