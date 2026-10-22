def matr_mult(matrix1, matrix2):
    col = []
    sum = 0
    lst = []
    mult_matrix = []
    #print(mult_matrix)
    for i in range(len(matrix1)):
        row = matrix1[i]
        for x in range(len(matrix2)):
            for j in range(len(matrix2[0])):
                col.append(matrix2[j][x])
            # print(row)
            # print(col)
            for k in range(0, len(row)):
                sum += row[k] * col[k]
            lst.append(sum)
            # print(sum)
            # print("")
            sum = 0
            col.clear()
        mult_matrix.append(lst)
        lst.clear()
        row.clear()
    return mult_matrix

print(matr_mult([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
