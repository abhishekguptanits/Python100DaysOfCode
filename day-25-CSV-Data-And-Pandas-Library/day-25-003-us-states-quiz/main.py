import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()         # Converts the String to Title Case

    if answer_state == "Exit" or "Quit":
        break
    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            xcor = int(state_data.x.item())
            ycor = int(state_data.y.item())
            t.goto(xcor, ycor)
            t.write(state_data.state.item())
            # t.write(answer_state)


# missed_states.csv
missed_states = []
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missing_states.csv")

