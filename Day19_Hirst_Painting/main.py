# import colorgram as cg
# color_list = cg.extract("image_hirst.jpg", 20)
# color_pallete = []
# color_tuple = ()
#
# for color in color_list:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_pallete.append(new_color)
#
# print(color_pallete)


color_list = [(249, 248, 248), (232, 241, 239), (1, 9, 30), (229, 235, 242),
              (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72),
              (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170),
              (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91),
              (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218)]

import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
screen = Screen()

t.colormode(255)

tim.penup()
x = -200
y = -200
tim.goto(x, y)
tim.pendown()
tim.speed("fastest")
tim.hideturtle()


def moving():
    global y
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    y = y + 30
    tim.goto(x, y)
    tim.pendown()

for _ in range(10):
    moving()

screen.exitonclick()
