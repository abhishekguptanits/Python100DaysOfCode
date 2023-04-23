import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral")
timmy_the_turtle.speed(3)
# timmy_the_turtle.forward(100)       #Move by 100 paces
# timmy_the_turtle.right(90)          #Turns right by 90 degree.


# # Challenge1: Draw a Square
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# # Challenge 2: Draw a dashed line
# for _ in range(20):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)


# # Challenge 3: Drawing different Shapes
# # Hint: Sum of internal angles of a polygon = (n-2)/180
# import random
# color_list = ["black", "coral", "green", "light salmon", "medium purple", "blue", "lemon chiffon", "cyan", "powder blue"]
# color_index = 0
# for n in range(3, 11):
#     sum_of_internal_angle = (n-2)*180
#     each_internal_angle = sum_of_internal_angle/n
#     external_angle = 180 - each_internal_angle
#     # external_angle can also be simply find by 360/n
#
#     # timmy_the_turtle.color(color_list[color_index])
#     # color_index += 1
#     timmy_the_turtle.color(random.choice(color_list))
#     while n>0:
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(external_angle)
#         n -= 1



# # Challenge 4: Generate a Random Walk
#
#
# import random
#
# color_list = ["black", "coral", "green", "light salmon", "medium purple", "blue", "lemon chiffon", "cyan", "powder blue"]
# direction = [0, 90, 180, 360]
#
# def random_walk():
#     timmy_the_turtle.width(20)
#     timmy_the_turtle.color(random.choice(color_list))
#
#     timmy_the_turtle.speed(10)
#     timmy_the_turtle.forward(40)
#
#     # To move to a random direction
#         # random_number = random.randint(1, 4)
#         # timmy_the_turtle.right(90*random_number)
#     timmy_the_turtle.setheading(random.choice(direction))
#
#
# for _ in range(200):
#     random_walk()







# # Challenge 4.1: Generate a Random Walk
#
#
# import random
# turtle.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color_tuple = (r, g, b)
#     return random_color_tuple
#
#
# direction = [0, 90, 180, 360]
#
#
# def random_walk():
#     timmy_the_turtle.width(20)
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.speed(10)
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(direction))
#
#
# for _ in range(200):
#     random_walk()











# Challenge 5: Draw a Spirograph
import random


turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


radius = 100
angle = 5

# timmy_the_turtle.speed("normal")
timmy_the_turtle.speed("fastest")
check = 0
for _ in range(int(360/angle)):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(radius)
    timmy_the_turtle.left(angle)

















# # Using external modules in Python
#
# import heroes
#
# print(heroes.gen())
#

screen = Screen()
screen.exitonclick()
