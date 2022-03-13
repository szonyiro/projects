import random
import turtle
from turtle import Turtle, Screen
import colorgram
turtle.colormode(255)
tim = Turtle()
# tim.shape("turtle")
tim.speed(10)
# tim.width(1)
# direction = [0, 90, 180, 270]
x_start = -375.00
y_start = -350.00


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def spot_row():
    tim.hideturtle()
    x = x_start
    y = y_start
    row = 0
    no_rows = 10
    for _ in range(no_rows):
        for _ in range(10):
            tim.penup()
            tim.goto(x, y)
            tim.dot(random.randint(25, 55), random.choice(color_list))
            x += 80
            tim.pendown()
        if row < no_rows - 1:
            x = x_start
            tim.penup()
            y += 80
            tim.goto(x, y)
            row += 1


color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
              (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90),
              (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55),
              (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
              (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210)]

spot_row()


screen = Screen()
screen.exitonclick()
