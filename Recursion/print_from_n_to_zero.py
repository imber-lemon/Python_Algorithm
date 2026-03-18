def n_to_zero(n):
    if n != 0:
        print(n)
        return n_to_zero(n - 1)
    else:
        return 0
print(n_to_zero(10))