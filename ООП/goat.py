class goat:
    def __init__(self, weight = 9, height = 1):
        self.weight = weight
        self.height = height

    def __str__(self):
        s = 'Вес:', str(self.weight), 'Рост', str(self.height)
        return s

    if self.weight <= 10 and