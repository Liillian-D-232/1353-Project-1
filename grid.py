
class Grid:
    def __init__(self, width, height) :
            self.width = width 
            self.height = height
            # store all the fish in the lake
            self.living_fish = []
            # store the fish that are dead and yet to be removed
            self.dead_fish = []
            # TODO: Create self.grid, a nested list of the given width
            # and height, every value is initialized to None
            self.grid = [[None for j in range(self.height)] for i in range(self.width)]