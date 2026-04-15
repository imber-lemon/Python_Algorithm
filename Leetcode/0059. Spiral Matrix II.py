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
    print(matrix)
    sp_m = []
    l = 0 # счетчик отступа
    num = matrix[0][0]
    for l in range(len(matrix) // 2 + 1):
        if num == matrix[l][l]:
            for i in range(l, len(matrix[l]) - l):
                sp_m.append(matrix[l][i])
            num = matrix[l][-1-l]
        if num == matrix[l][-l-1]:
            for i in range(1 + l, len(matrix) - l):
                sp_m.append(matrix[i][-1-l])
            num = matrix[-1-l][-1-l]
        if num == matrix[-1-l][-1-l]:
            for i in range(len(matrix[0])-2-l, l-1, -1):
                sp_m.append(matrix[-1-l][i])
            num = matrix[-1-l][l]
        if num == matrix[-1-l][l]:
            x = -1-l
            while matrix[x][l] not in sp_m:
                sp_m.append(matrix[x][l])
                x -= 1
            num = matrix[x+1][1+l]
            #print(num)
        l += 1
    return sp_m
print(spiral_matrixII(10))
