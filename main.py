import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Map Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = []
states_list = pandas.read_csv("50_states.csv")

all_states = states_list.state.to_list()

while len(answer) < 50:
    guess = screen.textinput(title = f"{len(answer)}/50 States Correct",
                             prompt="What's another state's name?").title()

    if guess == "Exit":
        break

    if guess in all_states:
        answer.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_list[states_list.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
        # t.write(state_data.state.item())

#States_to_learn.csv
missing_states = []
for state in all_states:
    if state not in answer:
        missing_states.append(state)

data_dict = {
    "States": missing_states
}

new_learn_data = pandas.DataFrame(data_dict)
new_learn_data.to_csv("States_to_learn.csv")

