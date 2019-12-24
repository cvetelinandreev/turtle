from turtle import *


def init():
    Screen().setup(width=1.0, height=1.0)
    Screen().tracer(8, 25)
    Screen().title("Spiral")

    colormode(255)
    reset();


def spiral(size):
    if size > 500:
        return

    fd(size)
    right(61)
    spiral(size + 3)


init()
spiral(10)
done()
