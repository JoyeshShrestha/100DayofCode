import turtle

import pandas
screen = turtle.Screen()
screen.title("U.S States Game")

image = "C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\day-25-us-states-game-start\\blank_states_img.gif"


screen.addshape(image)
turtle.shape(image)
# screen.exitonclick()

# def get_mouse_click_coor(x,y):
#     print(x,y)


# turtle.onscreenclick(get_mouse_click_coor)    


data = pandas.read_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\day-25-us-states-game-start\\50_states.csv")
all_states = data.state.to_list()
current_score = 0
guessed_state = []

while len(guessed_state)<50:
    answer_state = screen.textinput(title=f"{current_score}/50", prompt="What's another state's name?").title()
# print(answer_state)
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day025_CSV\\day-25-us-states-game-start\\states_to_learn.csv")
        print(missing_state)    
        break
    if answer_state in all_states:
        if answer_state not in guessed_state:
            current_score+=1
            state_data = data[data.state == answer_state]
        
            t = turtle.Turtle()
            t.hideturtle()
            t.penup() 
            t.goto((int(state_data.x),int(state_data.y)))
            t.write(answer_state)
            guessed_state.append(answer_state)
        
    else:
        pass
        
        
    # print(state_data)

# turtle.mainloop()

for state in all_states:
    if state in guessed_state:
        pass
    else:
        missed_state_data = data[data.state == state]

        
        
