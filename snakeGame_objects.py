import dudraw

class Object:
    """Base class for all objects on grid"""

    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.COLOR = color

    def __str__(self):
        return (f"coordinate: ({self.x}, {self.y}), RGB: {self.COLOR}")

    def __repr__(self):
        return self.__str__()
    
    def move(self, grid):
        pass

    def check_status(self, grid):
        pass

    def draw(self) :
        pass

class Food(Object):

    def __init__(self, x, y):
        super().__init__(x, y, self.COLOR)
        self.eaten = False

    def __str__(self) :
        return f"Food: " + super().__str__() + f" eaten: {self.eaten}"
    
    def __repr__(self) :
        return self.__str__()
    
    def is_eaten(self) :
        return self.eaten

    def draw( self ) :
        dudraw.set_pen_color( self.COLOR )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )

class Snakebody(Object):

    # dudraw.color

    def __init__(self, x, y):
        pass
