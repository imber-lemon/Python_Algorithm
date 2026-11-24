def matr_mult(mat1, mat2):
    sum_num = 0
    ret = []
    lst = []
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            for x in mat1[i]:
                for y in mat2[j]:
                    sum_num += x * y
            #     lst.append(sum_num)
            # ret.append(lst)
            # lst.clear()
            print(sum_num)
            sum_num = 0
    return ret

print(matr_mult([[1, 2],
                 [3, 4]], [[1, 2],[3, 4]]))