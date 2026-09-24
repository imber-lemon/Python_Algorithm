def is_into_triangle(triangle, point):
    s = [0, 0, 0]
    print(triangle[1][0], triangle[2][0], triangle[1][1], triangle[2][1])
    line = (((triangle[1][0] - triangle[2][0]) ** 2) + (triangle[1][1] - triangle[2][1]) ** 2) ** 0,5
    return line
print(is_into_triangle([[0, 2], [1, 4], [4, 7]], (1, 1)))