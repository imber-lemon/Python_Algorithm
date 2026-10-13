from nice_print import nice_print

def transportin_reverse(matrix):
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0]) - 1, len(matrix[0]) - i - 1, -1):
            print(i, j)
            matrix[i][j], matrix[i-1][j-1] = matrix[i-1][j-1], matrix[i][j]
    nice_print(matrix)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

transportin_reverse(matrix2)
