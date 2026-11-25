def matr_mult(mat1, mat2):
    col = []
    for i in range(0, len(mat1)):
        row = mat1[i]
        for j in range(len(mat2)):
            for h in range(len(mat2[0])):
                col.append(mat2[h][j])
            for k in range(len(col)):
                sum = col[k] * row[k]

            col.clear()

print(matr_mult([[1, 2], [3, 4]], [[1, 2], [3, 4]]))

"""
1     2               1     2
              *              
3     4               3     4
"""