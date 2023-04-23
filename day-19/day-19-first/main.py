from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


# To make the screen, start listening
screen.listen()


# Once it(the screen) starts listening, we have to bind a function
# that will be triggered, when a particular key is pressed on the keyboard.


# In order to bind a keystroke to an event in our code, we have to use an event listener


# turtle.onkey(fun, key)
# turtle.onkeyrelease(fun, key)
#     Parameters
#         fun – a function with no arguments or None
#         key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
#
#     Bind fun to key-release event of key. If fun is None, event bindings are removed.
#     Remark: in order to be able to register key-events, TurtleScreen must have the focus. (See method listen().)
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    # tim.setheading(tim.heading()+10)
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


# When we use a function as a argument then we don't actually add the parenthesis at the end.
# The parenthesis triggers the function to happen there and then
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear_screen)


# To stop the screen from disappearing, when we run it
screen.exitonclick()












































