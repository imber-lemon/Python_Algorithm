def smallest_el_in_sorted_matrix(matrix, k):
    matrix2 = []
    for i in range(0, len(matrix)):
        for x in matrix[i]:
            matrix2.append(x)
    matrix2.sort()
    return matrix2[k-1]
print(smallest_el_in_sorted_matrix([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
