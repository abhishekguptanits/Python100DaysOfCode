# # import turtle
# # turtle1 = turtle.Turtle()
#
# from turtle import Turtle, Screen
#
# # here the object name is given as timmy
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSlateGray", "DarkOliveGreen4")
# # timmy.shapesize(10)
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_rows(
    [
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

table.align = "l"

print(table)

