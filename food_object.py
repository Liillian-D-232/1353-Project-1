import dudraw

class Particle:
    def __init__(self, x, y) -> None:
        self.x_pos = x
        self.y_pos = y
        self.r = 120
        self.g = 120
        self.b = 120

    def draw(self):
        