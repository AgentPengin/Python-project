import turtle
import pandas

#font
FONT = ("Courier", 8, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True
correct_answers = 0
data = pandas.read_csv("50_states.csv")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
state_list = data["state"].to_list()
print(state_list)

check_state = {}
for state in state_list:
    check_state.update({state : False})

print(check_state)

def normalize_name(name):
    name = name.lower()
    name_parts = name.split()
    normalized_name_parts = [part.capitalize() for part in name_parts]
    normalized_name = " ".join(normalized_name_parts)
    return normalized_name

while game_is_on:
    if correct_answers == 50:
        break
    answer_state = screen.textinput(title = f"{correct_answers}/{len(data["state"])} States Correct", prompt = "What's another state name?")
    answer_state = normalize_name(answer_state)
    if (answer_state == "Exit"):
        missing_states = []
        for state in state_list:
            if check_state[state] == False:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in check_state and check_state[answer_state] == False:
        check_state[answer_state] = True
        correct_answers += 1
        x_coor_list = data[data["state"] == answer_state]["x"].to_list()
        y_coor_list = data[data["state"] == answer_state]["y"].to_list()
        x_coor = x_coor_list[0]
        y_coor = y_coor_list[0]
        pen.goto(x_coor,y_coor)
        pen.write(answer_state, align = "center", font = FONT)


# answer_state = screen.textinput(title = "Guess the State", prompt = "What's another state's name?")

turtle.exitonclick()
