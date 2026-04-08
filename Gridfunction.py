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

def create_world(X_scale: int = 50, Y_scale: int = 50):
    Width = int(int(X_scale)*5)
    Height = int(int(Y_scale)*5)
    dudraw.set_canvas_size(Width, Height)
    dudraw.set_x_scale(0, X_scale)
    dudraw.set_y_scale(0, Y_scale)
    grid_scale = [[EMPTY for j in range (X_scale)] for i in range (Y_scale)]
    return grid_scale
    
