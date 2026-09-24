def is_into_triangle(triangle, point):
    s = [0, 0, 0, 0]
    center_lines = [0, 0, 0]
    border_lines = [0, 0, 0]
    #print(triangle[0][0], triangle[1][0], triangle[0][1], triangle[1][1])
    for i in range(0, len(triangle) - 1):
        line = (((triangle[i][0] - point[0]) ** 2), (triangle[i][1] - point[1]) ** 2)
        print(line, triangle[i])
        line = (line[0] + line[1]) ** 0.5
        center_lines[i] = line
    line = (((triangle[-1][0] - point[0]) ** 2), (triangle[-1][1] - point[1]) ** 2)
    center_lines[-1] = (line[0] + line[1]) ** 0.5
    line = ()
    for i in range(0, len(triangle)-1):
        line = (((triangle[i][0] - triangle[i + 1][0]) ** 2), (triangle[i][1] - triangle[i + 1][1]) ** 2)
        border_lines[i] = (line[0] + line[1]) ** 0.5
    line = (((triangle[0][0] - triangle[-1][0]) ** 2), (triangle[0][1] - triangle[-1][1]) ** 2)
    border_lines[-1] = (line[0] + line[1]) ** 0.5


    for i in range(2):
        a = center_lines[i]
        b = center_lines[i + 1]
        c = border_lines[i]
        p = (a + b + c) / 2
        s[i] = (p * (p - a) * (p - b) * (p - c)) ** 0,5
    return center_lines, border_lines
print(is_into_triangle([[0, 2], [0, 7], [4, 7]], (2, 7)))