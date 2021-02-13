from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtles = [];

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_choice:
                print(f"You've won! The {user_choice} turtle is the winner!")
            else:
                print(f"You've lost! The {user_choice} turtle has lost!")
            is_race_on = False
        random_movement = random.randint(0, 10)
        turtle.forward(random_movement)

screen.exitonclick()
