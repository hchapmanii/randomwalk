import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
angles = [90, 180, 360, 0]


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    print(rgb)
    return rgb


def moving():
    tim.width(5)
    tim.speed("fast")
    # tim.color(random.choice(colours))
    tim.color(colors())
    tim.forward(30)
    tim.setheading(random.choice(angles))


for m in range(500):
    colors()
    moving()

my_screen = Screen()
my_screen.exitonclick()
