class Horse:
    def __init__(self, c, r):
        self.color = c
        self.rider = r

class Rider:
    def __init__(self, n):
        self.name = n


rider = Rider("Tomy")
horse = Horse("black", rider)

print(horse.rider.name)
