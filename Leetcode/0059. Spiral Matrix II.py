def spiral_matrixII(n):
    matrix = [[]]
    j = 0
    for i in range(1, n**2+1):
        if i % n == 0 and i != n**2:
            matrix[j].append(i)
            matrix.append([])
            j += 1
        else:
            matrix[j].append(i)
    return matrix
print(spiral_matrixII(4))
# 00, 01, 02, 12, 22, 21, 20, 10, 11
