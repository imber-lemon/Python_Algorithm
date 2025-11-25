# def nth_digit(n):
#     string = ""
#     for i in range(1, n + 1):
#         string += str(i)
#     return int(string[n-1])
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

def nth_digit(n):
    sum = 0
    len_n = 0
    for i in range(0, n):
        sum += len(str(i))
        if sum == n:
            return str(n)[0]
        elif sum > n:
            i = str(i)
            return i[sum-n-1]
print(nth_digit(11))