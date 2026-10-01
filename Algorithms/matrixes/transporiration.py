from nice_print import nice_print


def transportin(matrix):
    matrix_new = [[0] * len(matrix[0])] * len(matrix)
    # nice_print(matrix)
    # print("")
    # nice_print(matrix_new)
    for i in range(len(matrix)):
        for x in range(len(matrix[0])):
            matrix_new[x][i] = matrix[i][x]
            nice_print(matrix_new)
            print("""
            
            """)
    nice_print(matrix_new)

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

matrix_last = [[1, 5, 9, 13],
               [2, 6, 10, 14],
               [3, 7, 11, 15],
               [4, 8, 12, 16]]
transportin(matrix)