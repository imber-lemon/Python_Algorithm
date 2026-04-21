from classes.print_matrix import print_matrix


def spiral_matrix(matrix):
    print_matrix(matrix)
    sp_m = []
    num = matrix[0][0]
    l = 0 # счетчик отступа
    while l <= min(len(matrix), len(matrix[0])) // 2:
        if num == matrix[l][l] and len(sp_m) < len(matrix[0]) * len(matrix):
            for i in range(l, len(matrix[l]) - l):
                sp_m.append(matrix[l][i])
                # print(sp_m)
                # input()
            num = matrix[l][-1-l]
        if num == matrix[l][-1-l] and len(sp_m) < len(matrix[0]) * len(matrix):
            for i in range(1 + l, len(matrix) - l):
                sp_m.append(matrix[i][-1-l])
                # print(sp_m)
                # input()
            num = matrix[-1-l][-1-l]
        if num == matrix[-1-l][-1-l] and len(sp_m) < len(matrix[0]) * len(matrix):
            for i in range(len(matrix[0])-2-l, l-1, -1):
                sp_m.append(matrix[-1-l][i])
                # print(sp_m)
                # input()
            num = matrix[-1-l][l]
        if num == matrix[-1-l][l] and len(sp_m) < len(matrix[0]) * len(matrix):
            x = -2-l
            while matrix[x][l] not in sp_m:
                sp_m.append(matrix[x][l])
                x -= 1
                # print(sp_m)
                # input()
            #print(num)
        l += 1
        num = matrix[l][l]
            # print(l, matrix[l][l])
            # input()
    return sp_m
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrix5 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
matrix6 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]
print(spiral_matrix([[1, 2, 3], [4, 5, 6]]))
