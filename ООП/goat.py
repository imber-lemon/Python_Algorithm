class Goat:
    def __init__(self, weight = 9, height = 1):
        self.weight = weight
        self.height = height

    def __str__(self):
        s = f"Вес: {self.weight}, Рост: {self.height}"
        return s

masha = Goat(13, 4)
print(masha)