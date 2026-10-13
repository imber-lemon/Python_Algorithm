def nice_print(matrix):
    for i in range(len(matrix)):
        s = " "
        for x in matrix[i]:
            if x < 10:
                s += " " + str(x) + " "
            elif x >= 10 and x < 100:
                s += str(x) + " "
            elif x >= 100 and x < 1000:
                s += str(x)
            s += " "
        print(s)
#nice_print([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [100, 200, 300, 400]])
