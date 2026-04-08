import dudraw
import random

EMPTY = 0
SNAKEHEAD = 1
SNAKEBODY = 2
FOODPELLET = 3


# def Set_Scale():
#     scale = input("What do you want the canvas size to be?")
#     while not ((scale.isnumeric()) and (int(scale) >= 100) and (int(scale) <= 1000)):
#         scale = input("What do you want the canvas size to be? answer Must Be > 100 and < 1000")
#     X_scale = int(int(scale)//5)
#     Y_scale = int(int(scale)//5)
#     return X_scale, Y_scale

def create_world(X_scale: int = 20, Y_scale: int = 20):
    Width = int(int(X_scale)*25)
    Height = int(int(Y_scale)*25)
    dudraw.set_canvas_size(Width, Height)
    dudraw.set_x_scale(0, X_scale)
    dudraw.set_y_scale(0, Y_scale)
    grid_scale = [[EMPTY for j in range (X_scale)] for i in range (Y_scale)]
    return grid_scale

direction = 0

class square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    def draw(self):
        dudraw.set_pen_color_rgb(*self.color)
        dudraw.filled_square(self.x, self.y, self.size)




def main():
    create_world()
    dudraw.show(500)


if __name__ == '__main__':
    main()
    
