def spiral_print(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rev_mat = [[0] * (cols * 2 - 1) for _ in range(rows * 2 - 1)]
    #print(rev_mat)
    i = 0
    j = cols - 1
    for x in range(rows):
        for y in range(cols):
            #print("i:", i, "j:", j, "       ", "x:", x, "y:", y)
            rev_mat[i][j] = matrix[x][y]
            i += 1
            j += 1
        i -= (cols - 1)
        j -= (cols + 1)
        #print(rev_mat)

    return rev_mat

mat = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
       [13, 14, 15, 16]]

mat2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print(spiral_print(mat2))
