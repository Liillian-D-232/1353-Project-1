from DoublyLinkedList import DoublyLinkedList as DLL
import random
import snakeGame_objects

class Grid:
    def __init__(self, width, height) :
            self.width = width 
            self.height = height
            # store all the fish in the lake
            self.uneaten_food = DLL()
            # store the fish that are dead and yet to be removed
            self.eaten_food = DLL()
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
            self.uneaten_food.add_last(new_apple)

    def eat_food( self, x, y ) :
        # TODO: Determine the fish at this location.
        the_food = self.grid[x][y]
        # Change its .dead instance variable to True
        the_food.eaten = True
        # Set the grid location to None
        self.grid[x][y] = None
        # append this fish to the list of dead fish.
        self.eaten_food.add_last(the_food)

    def remove_eaten_food(self):
        # TODO: traverse the list of dead_fish. For each one,
        # remove it from the list of living_fish. Then clear
        # the list of dead_fish.
        for _ in range(self.eaten_food.size):
            if self.eaten_food.get(_) in self.uneaten_food:
                self.uneaten_food.remove_at_index(self.eaten_food.get(_))
        
        for _ in range(self.eaten_food.size):
            self.eaten_food.remove_first()

    def draw(self):
        """Draw the current minnows and trouts in the lake"""
        # TODO: Write nested for loops which iterate over the grid cells of the lake
        #    If the cell value is None, draw a lake square
        #    Otherwise the cell value is a fish object so ask the fish to draw itself
        for i in range(self.width):
            for j in range(self.height):
                if self.grid[i][j] is None:
                    pass
                else:
                    obj = self.grid[i][j]
                    obj.draw()

    def SpawnSnake(self):
        self.snakes = []
        for i in range(2):
            self.snakes.append(snakeGame_objects.Snake(10, 5-i))
            # print(self.snakes[i])
        for i in range(len(self.snakes)):
            if i > 0:
                self.snakes[i].set_target(self.snakes[i-1])
            else:
                self.snakes[i].set_target(None)
        for snake in self.snakes:
            snake.draw()

    def SnakeMove(self, dir):
        if dir == 1:
            self.snakes[0].y_pos += 1
        elif dir == 2:
            self.snakes[0].x_pos -= 1
        elif dir == 3:
            self.snakes[0].y_pos -= 1
        elif dir == 4:
            self.snakes[0].x_pos += 1
        elif dir == 0:
            self.snakes[0].x_pos += 1
                
        for snake in self.snakes:
            if (snake.target_x is not None) and (snake.target_y is not None):
                x_diff = (snake.target_x - snake.x_pos)
                y_diff = (snake.target_y - snake.y_pos)
                self.x_position += x_diff
                self.y_position += y_diff
            snake.draw()