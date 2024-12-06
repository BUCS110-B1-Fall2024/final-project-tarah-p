class City:
    def __init__(self):
        self.green_level = 0  # Represents progress towards a sustainable city.

    def upgrade(self):
        self.green_level += 1

    def get_status(self):
        return f"City Green Level: {self.green_level}"
