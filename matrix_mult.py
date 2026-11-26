def matr_mult(mat1, mat2):
    res_mat = []
    col = []
    sum = 0
    lst = []
    for i in range(0, len(mat1)):
        row = mat1[i]
        for j in range(len(mat2[0])):
            for h in range(len(mat2)):
                col.append(mat2[h][j])
            for k in range(len(row)):
                sum += col[k] * row[k]
            lst.append(sum)
            sum = 0
            col.clear()
        lt = [0] * len(lst)
        for m in range(len(lst)):
            lt[m] = lst[m]
        res_mat.append(lt)
        lst.clear()
        row.clear()
    return res_mat
print(matr_mult([[1, 2], [3, 4], [3, 4]], [[5, 6, 7], [7, 8, 9]]))

""" 
1     2               1     2
              *              
3     4               3     4
"""