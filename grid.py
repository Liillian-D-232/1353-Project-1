import random
import snakeGame_objects

class Grid:
    def __init__(self, width, height) :
            self.width = width 
            self.height = height
            # store all the fish in the lake
            self.uneaten_food = []
            # store the fish that are dead and yet to be removed
            self.eaten_food = []
            # TODO: Create self.grid, a nested list of the given width
            # and height, every value is initialized to None
            self.grid = [[None for j in range(self.height)] for i in range(self.width)]
    
    def spawn_food(self, food_type):
        """Randomly choose beginning location of food objects."""
        spawned = False
        while not spawned:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if self.grid[x][y] == None:
                spawned = True
                self.add_new_food( food_type, x, y )

    def add_new_food( self, food_type, x, y ) :
        if food_type == "apple":
            # TODO: instantiate a new Minnow object,
            # store a reference to it in the correct grid location
            # Append the new minnow to the list of living fish
            new_apple = snakeGame_objects.Food(x,y)
            self.grid[x][y] = new_apple
            self.uneaten_food.append(new_apple)