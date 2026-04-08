import dudraw

class Particle:
    def __init__(self, x, y, color) -> None:
        self.x_pos = x
        self.y_pos = y
        self.color = color

    def draw(self):
        dudraw.set_pen_color_rgb(*self.color)
        dudraw.filled_square(self.x_pos, self.y_pos, 15)

class Food(Particle):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        
