def happy_num(n):
    sums = set()
    sum = 0
    sums.add(n)
    while sum not in sums:
        n = str(n)
        for i in range(0, len(n)):
            sum += int(n[i]) ** 2
        if sum == 1:
            return True
        elif sum in sums:
            return False
        else:
            sums.add(sum)
            n = sum
            sum = 0
    return False
print(happy_num(2))