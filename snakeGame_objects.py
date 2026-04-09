import dudraw

class Object:
    """Base class for all objects on grid"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return (f"coordinate: ({self.x}, {self.y}), RGB: {None}")

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
        super().__init__(x, y)
        self.eaten = False

    def __str__(self) :
        return f"Food: " + super().__str__() + f" eaten: {self.eaten}"
    
    def __repr__(self) :
        return self.__str__()
    
    def is_eaten(self) :
        return self.eaten

    def draw( self ) :
        dudraw.set_pen_color( dudraw.RED )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )

'''class Snakebody(Object):

    # dudraw.color

    def __init__(self, x, y, num):
        super().__init__(x, y)
        self.num = num

    def __str__(self):
        return f"Segment number: {self.num}" 

    def move(self, grid):
        self.x = #x of pervious node
        self.y = #y of pervious node
        
    def draw( self ) :
        dudraw.set_pen_color( self.COLOR )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )

class Snakehead(Object):

    dudraw.color

    def __init__(self, x, y, direction)
        super().__init__(x, y)
        self.direction = direction

    def __str__(self):
        return f"Position: {x, y}" 

    def move(self, grid):
        if self.direction = UP
            y += 1
        elif self.direction = DOWN
            y -= 1
        elif self.direction = RIGHT
            x += 1
        elif self.direction = LEFT
            x -= 1
        
    def draw( self ) :
        dudraw.set_pen_color( self.COLOR )
        dudraw.filled_rectangle( self.x+0.5, self.y+0.5, 0.45, 0.45 )
'''