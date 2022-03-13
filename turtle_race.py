import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "purple", "green", "blue", "pink"]
x_start = -225
y_start = -90


race_is_on = True
turtles = []
x = x_start
y = y_start

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.speed("slow")
    y += 30
    turtles.append(new_turtle)
    # print(new_turtle)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")

while race_is_on:
    for turtlex in turtles:
        # turtles[2].forward(0.2)  # pink turtle always wins cheat
        turtlex.forward(random.randint(0, 12))
        if turtlex.xcor() > 230:
            race_is_on = False
            print(f"The winner of the race is: {turtlex.pencolor().upper()}")
            if user_bet == turtlex.pencolor():
                print(f"Your bet was: {user_bet.upper()}. You win")
            else:
                print(f"Your bet was {user_bet.upper()}. You lose, better luck next time")


screen.exitonclick()

