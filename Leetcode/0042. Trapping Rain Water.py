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
# print(rain([0,1,0,2,1,0,1,3,2,1,2,1]))

def rain(height):
    lst = []
    w1 = height[0]
    summ = 0
    i = 1
    while i < len(lst) - 1:
        if w1 > height[i]:
            lst.append(height[i])
            print(lst)
        else:
            summ += len(lst) * max(lst) - sum(lst)
            print(summ)
            w1 = height[i]
        i += 1
print(rain([0,1,0,2,1,0,1,3,2,1,2,1]))