from turtle import *
import sys
import logging

sys.setrecursionlimit(4000)

import random

import gc



def init(initturtle):
    screen = initturtle.getscreen()
    screen.setup(width=1.0, height=1.0)
    screen.tracer(0, 0)
    screen.title("Context free")

    colormode(255)
    initturtle.reset()
    initturtle.pensize(3)
    initturtle.pencolor((101, 67, 33))
    initturtle.setheading(90)
    initturtle.penup()
    initturtle.goto(0, -100)

def increment_green(turtle):
    currentcolor = turtle.pencolor()
    turtle.pencolor((int(currentcolor[0]), int(currentcolor[1] + 3) if currentcolor[1] < 250 else 250, int(currentcolor[2])))

def spiral(spiralturtle, size, direction):
    if size < 1:
        del spiralturtle
        gc.collect()
        return

    spiralturtle.down()
    increment_green(spiralturtle)
    spiralturtle.fd(size)

    spiralturtle.up()
    spiralturtle.fd(2)

    angle = 7
    if direction == 'left':
        spiralturtle.left(angle)
    elif direction == 'right':
        spiralturtle.right(angle)

    newsize = size * 0.96

    rand = random.random();
    if (rand < 0.20):
        newturtle = spiralturtle.clone()
        if direction == 'left':
            newturtle.right(45)
            spiral(newturtle, newsize, 'right')
        elif direction == 'right':
            newturtle.left(45)
            spiral(newturtle, newsize, 'left')


    spiral(spiralturtle, newsize, direction)


t = Turtle()
init(t)
spiral(t, 15, 'left')
done()
