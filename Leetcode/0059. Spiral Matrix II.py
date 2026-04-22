from classes.print_matrix import print_matrix


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
    # print_matrix(matrix)
    sp_m = []
    l = 0
    while l <= (min(len(matrix), len(matrix[0])) - 1) // 2:
        for i in range(l, len(matrix[0]) - l):
            sp_m.append(matrix[l][i])
        for i in range(l + 1, len(matrix) - l):
            sp_m.append(matrix[i][-1-l])
        if len(matrix) - 1 - l != l:
            for i in range(len(matrix[0]) - 2 - l, l - 1, -1):
                sp_m.append(matrix[-1-l][i])
        if len(matrix[0]) - 1 - l != l:
            for i in range(len(matrix) - 2 - l, l, -1):
                sp_m.append(matrix[i][l])
        l += 1
    return sp_m

print(spiral_matrixII(1))
