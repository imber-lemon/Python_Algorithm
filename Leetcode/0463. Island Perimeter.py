def island_perimeter(grid):
    per = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                # print(i, j)
                # # print(grid[i+1][j], grid[i-1][j],grid[i][j+1], grid[i][j-1])
                # print("")
                if i > 0:
                    if grid[i - 1][j] == 0:
                        per += 1
                else:
                    per += 1

                if i < len(grid) - 1:
                    if grid[i + 1][j] == 0:
                        per += 1
                else:
                    per += 1

                if j > 0:
                    if grid[i][j - 1] == 0:
                        per += 1
                else:
                    per += 1

                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] == 0:
                        per += 1
                else:
                    per += 1
                # print(per)
                # print("")
    return per
print(island_perimeter([[0,1,0,0],
                        [1,1,1,0],
                        [0,1,0,0],
                        [1,1,0,0]]))


# if i + 1 != len(grid) - 1 and i + 1 != 0:
#     if grid[i + 1][j] == 0:
#         per += 1
# else:
#     per += 1
# if i - 1 == len(grid) - 1 and i - 1 != 0:
#     if grid[i - 1][j] == 0:
#         per += 1
# else:
#     per += 1
# if j + 1 == len(grid) - 1 and j + 1 != 0:
#     if grid[i][j + 1] == 0:
#         per += 1
# else:
#     per += 1
# if j - 1 == len(grid) - 1 and j - 1 != 0:
#     if grid[i][j - 1] == 0:
#         per += 1
# else:
#     per += 1
# print(per)
