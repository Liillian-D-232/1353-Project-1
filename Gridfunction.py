import dudraw
import random
import snakeGame_objects

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
BACKGROUND = dudraw.Color(62, 70,  73)

# def Set_Scale():
#     scale = input("What do you want the canvas size to be?")
#     while not ((scale.isnumeric()) and (int(scale) >= 100) and (int(scale) <= 1000)):
#         scale = input("What do you want the canvas size to be? answer Must Be > 100 and < 1000")
#     X_scale = int(int(scale)//5)
#     Y_scale = int(int(scale)//5)
#     return X_scale, Y_scale

def create_world(X_scale: int = 20, Y_scale: int = 20):
    dudraw.set_canvas_size( CANVAS_X, CANVAS_Y )
    dudraw.set_x_scale( 0, WIDTH )
    dudraw.set_y_scale( 0, HEIGHT )
    # Width = int(int(X_scale)*30)
    # Height = int(int(Y_scale)*30)
    # dudraw.set_canvas_size(Width, Height)
    # dudraw.set_x_scale(0, X_scale)
    # dudraw.set_y_scale(0, Y_scale)
    # grid_scale = [[EMPTY for j in range (X_scale)] for i in range (Y_scale)]
    # return grid_scale

def main():
    create_world()
    limit = 20 #number of frames to allow to pass before snake moves
    timer = 0  #a timer to keep track of number of frames that passed
    while True:
        timer += 1
        #process keyboard press here
        if timer == limit:
            timer = 0
            #draw and move the snake
            #check to see if snake ate the fruit
            #check if the snake self intersects

        dudraw.show(40)

if __name__ == '__main__':
    main()
    
