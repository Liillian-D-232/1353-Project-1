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

    def is_dead(self) -> bool:
        return False


class Object:
    """Base class for all objects on grid"""

    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.color = color

    def __str__(self):
        return (f"coordinate: ({self.x}, {self.y}), RGB: {self.color}")

    def __repr__(self):
        return self.__str__()
    
    def move(self, grid):
        pass

    def check_status(self, grid):
        pass

    def draw(self) :
        pass

class Food(Object):

    dudraw.color

    def __init__(self, x, y):
        super().__init__(x, y)
        self.eaten = False

    def __str__(self) :
        return f"Food: " + super().__str__() + f" eaten: {self.eaten}"
    
    def __repr__(self) :
        return self.__str__()
    
    def is_eaten(self) :
        return self.eaten

    def draw( self ) :
        dudraw.set_pen_color( Minnow.MINNOW )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )

class Snakebody(Object):

    dudraw.color

    def __init__(self, x, y)
