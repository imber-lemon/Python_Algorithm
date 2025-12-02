def max_water(height):
    max_sq = 0
    for i in range(0, len(height)):
        for x in range(len(height)-1, -1, -1):
            if (x - i) * min(height[x], height[i]) > max_sq:
                max_sq = (x - i) * min(height[x], height[i])
    return max_sq
