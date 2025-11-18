def happy_num(n):
    lst = set()
    sum = 0
    lst.add(n)
    while sum not in lst:
        n = str(n)
        for i in range(0, len(n)):
            sum += int(n[i]) ** 2
        if sum == 1:
            return True
        elif sum in lst:
            return False
        else:
            lst.add(sum)
            n = sum
            sum = 0
    return False
print(happy_num(2))