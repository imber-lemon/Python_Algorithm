def matrix_search(matrix, target):
    x = len(matrix[0]) // 2
    y = len(matrix) // 2
    print(matrix[y][x])
    while matrix[y][x] != target:
        if matrix[y][x] > target:
            matrix = matrix[y::]
            print(matrix)
mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
mat = mat[1::][::]
print(mat)
#matrix_search(mat, 3)