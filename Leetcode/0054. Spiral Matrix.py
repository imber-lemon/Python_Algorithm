from classes.print_matrix import print_matrix

def spiral_matrix(matrix):
    print_matrix(matrix)
    sp_m = []
    num = matrix[0][0]
    for l in range(len(matrix) // 2):
        if num == matrix[0][0]:
            for i in range(0, len(matrix[0])):
                sp_m.append(matrix[0][i])
            num = matrix[0][-1]
        if num == matrix[0][-1]:
            for i in range(1, len(matrix)):
                sp_m.append(matrix[i][-1])
            num = matrix[-1][-1]
        if num == matrix[-1][-1]:
            for i in range(len(matrix[0])-2, -1, -1):
                sp_m.append(matrix[-1][i])
            num = matrix[-1][0]
        if num == matrix[-1][0]:
            x = -2
            while matrix[x][0] not in sp_m:
                sp_m.append(matrix[x][0])
                x -= 1
        return sp_m

print(spiral_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
