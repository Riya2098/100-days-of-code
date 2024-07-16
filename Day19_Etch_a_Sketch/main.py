import random
import turtle as t

screen = t.Screen()
screen.setup(width=500, height=400)
is_race = False
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Choose a color: ")

colors = ['red', 'green', 'pink', 'blue', 'orange', 'purple']
y_positions = [80, 40, 0, -40, -80, -120]
all_turtles = []

for i in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.speed('fast')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The winning turtle is {winning_turtle}")
            else:
                print(f"You lost, The winning turtle is {winning_turtle}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
