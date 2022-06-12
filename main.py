import random
import turtle
from turtle import Turtle, Screen
from tkinter import *
from tkinter import messagebox



screen = Screen()

continue_race = False
screen.setup(width=500, height=400)
screen.title('Turtle Racing!')
user_bet = turtle.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
start_coords = [-230, -70]
all_turtles = []


for color in colors:
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(color)
    coords = tuple(start_coords)
    new_turtle.goto(coords)
    start_coords[1] += 30
    all_turtles.append(new_turtle)


if user_bet:
    continue_race = True

while continue_race:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            continue_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                final_prompt = 'You Win!'
            else:
                final_prompt = 'You lose.'
            messagebox.showinfo('Winning turtle', f'{final_prompt} The winning turtle was {winning_color}.')


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)












# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.backward(10)
#
# def tilt_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def tilt_counterclockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear_canvas():
#     turtle.resetscreen()
#
#
# screen.listen()
# # when passing function into function, do not use parenthesis
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='a', fun=tilt_clockwise)
# screen.onkey(key='d', fun=tilt_counterclockwise)
# screen.onkey(key='c', fun=clear_canvas)

screen.exitonclick()