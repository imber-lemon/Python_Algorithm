def matrix_rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    lst = []
    for i in range(cols):
        for j in range(rows-1, -1, -1):
            lst.append(matrix[j][i])
        print(lst)
        for x in range(len(matrix[0])):
            matrix[i][x] = lst[x]
        lst.clear()
        print(matrix)
# matrix_rotate([[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]])
