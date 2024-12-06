class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.eco_points = 0

    def add_points(self, points):
        self.eco_points += points

    def reset_points(self):
        self.eco_points = 0
