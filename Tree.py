from turtle import *
import sys

sys.setrecursionlimit(4000)

import random


def init(initturtle):
    screen = initturtle.getscreen()
    screen.setup(width=1.0, height=1.0)
    screen.tracer(0, 0)
    screen.title("Tree")

    colormode(255)
    initturtle.reset()
    initturtle.pensize(3)
    initturtle.pencolor((101, 67, 33))
    initturtle.setheading(90)
    initturtle.penup()
    initturtle.goto(0, -200)


def increment_green(turtle):
    currentcolor = turtle.pencolor()
    turtle.pencolor(
        (int(currentcolor[0]), int(currentcolor[1] + 1) if currentcolor[1] < 250 else 250, int(currentcolor[2])))


def spiral(spiralturtle, size, direction):
    if size < 1:
        return

    increment_green(spiralturtle)
    spiralturtle.dot(size)
    spiralturtle.fd(size * 0.4)

    angle = 1
    if direction == 'left':
        spiralturtle.left(angle)
    elif direction == 'right':
        spiralturtle.right(angle)

    newsize = size * 0.99

    heading = spiralturtle.heading()
    position = spiralturtle.pos()

    rand = random.random()
    if rand < 0.05:
        if direction == 'left':
            spiralturtle.right(45)
            spiral(spiralturtle, newsize, 'right')
        elif direction == 'right':
            spiralturtle.left(45)
            spiral(spiralturtle, newsize, 'left')
        spiralturtle.setheading(heading)
        spiralturtle.setposition(position)

    spiral(spiralturtle, newsize, direction)
    spiralturtle.setheading(heading)
    spiralturtle.setposition(position)


t = Turtle()
init(t)
spiral(t, 15, 'left')
done()
