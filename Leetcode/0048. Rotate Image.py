def matrix_rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    s = []
    for i in range(cols):
        for j in range(rows-1, -1, -1):
            s.append(matrix[j][i])
        print(s)
        s.clear()
matrix_rotate([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])