import random as rd
# def find_p():
#     c = 1
#     for i in range(3, 10000000, 4):
#         c -= 1 / i
#     for i in range(5, 10000000, 4):
#         c += 1 / i
#     return 4 * c
# print(find_p())
def monte_carlo():
    inside = 0
    all_points = 0
    t = 1000000
    for i in range(t):
        x = rd.randint(-t, t) / t
        y = rd.randint(-t, t) / t
        if x ** 2 + y ** 2 <= 1:
            inside += 1
        all_points += 1
    return 4 * inside / all_points
print(monte_carlo())
