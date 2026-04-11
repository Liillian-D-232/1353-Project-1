from DoublyLinkedList import DoublyLinkedList as DLL
import dudraw
import random
import snakeGame_objects
from grid import Grid

EMPTY = 0
SNAKEHEAD = 1
SNAKEBODY = 2
FOODPELLET = 3

# Constants for dudraw canvas size
CANVAS_X = 600
CANVAS_Y = 600

# Constants for width and height of simulation grid
WIDTH = 20
HEIGHT = 20

# Constant for the canvas background color
BACKGROUND = dudraw.Color(150, 150, 150)

# def Set_Scale():
#     scale = input("What do you want the canvas size to be?")
#     while not ((scale.isnumeric()) and (int(scale) >= 100) and (int(scale) <= 1000)):
#         scale = input("What do you want the canvas size to be? answer Must Be > 100 and < 1000")
#     X_scale = int(int(scale)//5)
#     Y_scale = int(int(scale)//5)
#     return X_scale, Y_scale

def create_world():
    dudraw.set_canvas_size( CANVAS_X, CANVAS_Y )
    dudraw.set_x_scale( 0, WIDTH )
    dudraw.set_y_scale( 0, HEIGHT )
    dudraw.clear(BACKGROUND)
    # Width = int(int(X_scale)*30)
    # Height = int(int(Y_scale)*30)
    # dudraw.set_canvas_size(Width, Height)
    # dudraw.set_x_scale(0, X_scale)
    # dudraw.set_y_scale(0, Y_scale)
    # grid_scale = [[EMPTY for j in range (X_scale)] for i in range (Y_scale)]
    # return grid_scale

def main():
    create_world()
    the_grid = Grid(WIDTH, HEIGHT)

    limit = 20 #number of frames to allow to pass before snake moves
    timer = 0  #a timer to keep track of number of frames that passed

    num_food = 1
    key = dudraw.next_key_typed()
    while key != 'q':
        timer += 1
        if (the_grid.uneaten_food.size) < 1:
            the_grid.spawn_food("apple")
        the_grid.draw()
        #process keyboard press here
        if timer == limit:
            timer = 0
            
            #check to see if snake ate the fruit
            #check if the snake self intersects

        dudraw.show(40)

if __name__ == '__main__':
    main()
    
