def from_any_to_any(num, sys_relay, sys_into):
    lst = []
    num_10 = 0
    st = 0
    for i in range(len(str(num)) - 1, -1, -1):
        if int(str(num)[i]) == sys_relay:
            return "Ошибка"
            break
        else:
            num_10 += int(str(num)[i]) * sys_relay ** st
            st += 1
    print(num_10)
    while num_10 >= sys_into:
        lst.append(num_10 % sys_into)
        num_10 //= sys_into
    lst.append(num_10)
    res = ""
    for i in lst[::-1]:
        res += str(i)
    return res
print(from_any_to_any(12, 2, 2))