class Task:
    def __init__(self, description, points):
        self.description = description
        self.points = points
        self.completed = False

    def complete(self):
        self.completed = True
        return self.points
