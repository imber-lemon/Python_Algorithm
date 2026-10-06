from nice_print import nice_print
import random as rd

def transportin(matrix):
    # matrix_new = []
    # for i in range(len(matrix)):
    #     matrix_new.append([0] * len(matrix))

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    nice_print(matrix)

# matrix = []
# for i in range(5):
#     lst = [0, 0, 0, 0, 0]
#     for j in range(5):
#         lst[j] = rd.randint(0, 10)
#     matrix.append(lst)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
nice_print(matrix)
print(" ")
transportin(matrix)
