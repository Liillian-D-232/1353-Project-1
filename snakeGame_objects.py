import dudraw

class Particle:
    def __init__(self, x, y) -> None:
        self.x_pos = x
        self.y_pos = y
        self.r = 120
        self.g = 120
        self.b = 120

    def draw(self):
        dudraw.filled_square(self.x_pos, self.y_pos, 15)

class Food(Particle):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    
    def is_dead(self) -> bool:
        return False


class Fish:
    """Base class for all objects on grid"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.r = 120
        self.g = 120
        self.b = 120

    def __str__(self):
        return (f"coordinate: ({self.x}, {self.y}), RGB: {self.r,self.g,self.b}")

    def __repr__(self):
        return self.__str__()
    
    def move(self, lake):
        pass

    def check_status(self, lake):
        pass

    def draw(self) :
        pass