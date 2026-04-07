def tar_in_matrix(matrix, target):
    for i in range(0, len(matrix)):
        print(matrix[i])
    print(' ')
    for i in range(0, len(matrix)):
        for j in matrix[i]:
            if j == target:
                return True
    return False

print(tar_in_matrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))