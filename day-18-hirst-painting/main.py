# import colorgram
#
#
# # Extract 30 colors from an image
# colors = colorgram.extract("hirst_colours.jpg", 30)
# rgb_list = []
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     rgb_list.append((red, green, blue))
#
#
# print(rgb_list)
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
color_list = [(243, 250, 246), (236, 244, 250), (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199)]


start_x = -200
start_y = -200

timmy = Turtle(shape="turtle", visible=False)
timmy.shape("classic")
timmy.hideturtle()
timmy.speed("fastest")

for _ in range(10):
    timmy.penup()
    timmy.goto(start_x, start_y)
    timmy.pendown()
    timmy.dot(20, random.choice(color_list))
    start_y += 50
    for _ in range(10):
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20, random.choice(color_list))







screen = Screen()
screen.exitonclick()










