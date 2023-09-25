from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ["purple", "red", "blue", "brown", "pink", "black", "yellow", "green"]
angles = [90, 180, 270, 0]


def moving():
    tim.width(5)
    tim.speed("fast")
    tim.color(random.choice(colours))
    tim.forward(50)
    tim.setheading(random.choice(angles))


for m in range(500):
    moving()

my_screen = Screen()
my_screen.exitonclick()
