from turtle import *
import random
import sys

sys.setrecursionlimit(4000)


def getturtle():
    initturtle = Turtle()
    screen = initturtle.getscreen()
    screen.setup(width=1.0, height=1.0)
    screen.tracer(0, 0)
    screen.title("Venes")

    screen.colormode(255)
    initturtle.reset()
    initturtle.setheading(90)
    initturtle.penup()
    initturtle.goto(0, -200)

    return initturtle


def rotate(turtle, angle, direction):
    if direction == 'left':
        turtle.left(angle)
    elif direction == 'right':
        turtle.right(angle)


def spiral(spiralturtle, size, direction):
    if size < 1:
        return

    heading = spiralturtle.heading()
    position = spiralturtle.pos()

    rand = random.random()
    probability_of_branching = 0.05
    if rand < probability_of_branching:
        # branch
        rotate(spiralturtle, 90, direction)
        sizeofbranch = size * 0.6
        spiral(spiralturtle, sizeofbranch, direction)

        spiralturtle.setheading(heading)
        spiralturtle.setposition(position)

        # flip for the next branch
        sizeafterbranching = size * 0.9
        if direction == 'left':
            spiral(spiralturtle, sizeafterbranching, 'right')
        elif direction == 'right':
            spiral(spiralturtle, sizeafterbranching, 'left')
    else:
        spiralturtle.dot(size)
        spiralturtle.fd(size * 0.4)

        rotate(spiralturtle, 1, direction)
        spiral(spiralturtle, size * 0.99, direction)

    spiralturtle.setheading(heading)
    spiralturtle.setposition(position)


t = getturtle()
spiral(t, 20, 'left')
t.getscreen().mainloop()
