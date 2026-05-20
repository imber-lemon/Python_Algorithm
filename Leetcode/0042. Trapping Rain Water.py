# def rain(height):
#     summary = 0
#     w1 = height[0]
#     lst = []
#     for i in range(1, len(height)):
#         if height[i] < max(lst):
#             lst.append(height[i])
#         else:
#             print(w1, height[i])
#             summary += min(height[i], w1) * (i - height.index(w1)) - sum(lst)
#             lst.clear()
#             w1 = height[i]
#     return "итог:", summary
# print(rain([4,2,0,3,2,5]))

def rain(height):
    lst = []
    w1 = height[0]
    summ = 0
    i = 0
    while i < len(lst) - 1:
        while height[i] >