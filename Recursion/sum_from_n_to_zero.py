def sum_from_n_to_zero(n):
    if n == 1:
        return 1
    else:
        return n + sum_from_n_to_zero(n - 1)
print(sum_from_n_to_zero(9))