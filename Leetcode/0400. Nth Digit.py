def nth_digit(n):
    string = ""
    for i in range(1, n + 1):
        string += str(i)
    return int(string[n-1])
# print(nth_digit(200))

# def nth_digit(n):
#     string = ""
#     sum = 0
#     len_n = 0
#     while sum < n:
#         sum += 9 * 10 ** len_n
#         len_n += 1
#     for i in range(1, sum + 1):
#         string += str(i)
#     return int(string[n-1])
# print(nth_digit(100000000))

def nth_digit2(n):
    sum = 0
    for i in range(0, n):
        sum += len(str(i))
        if sum == n:
            ans = str(n)[0]
            return int(ans)
        elif sum > n:
            i = str(i)
            ans = i[1]
            ans = int(ans)
            return int(i[1])
print(nth_digit2(17))
