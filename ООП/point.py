class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def calculate_distance(self, x, y):
        dist = ((x - self.x) ** 2 + (y - self.y) ** 2) ** 0.5
        return dist

    def reset(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

p1 = Point(2, 2)
print(p1.reset())
