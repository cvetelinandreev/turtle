from turtle import *


def init():
    Screen().setup(width=1.0, height=1.0)
    Screen().tracer(0, 0)
    colormode(255)
    reset();


def fern(size, minsize, anglefactor):
    if size < minsize:
        return

    fd(size * 0.05)
    left(80 * anglefactor)
    fern(size * 0.35, minsize, anglefactor)
    right(82 * anglefactor)
    fd(size * 0.05)
    right(80 * anglefactor)
    fern(size * 0.35, minsize, -anglefactor)
    left(78 * anglefactor)
    fern(size * 0.9, minsize, anglefactor)
    left(2 * anglefactor)
    back(size * 0.05)
    left(2 * anglefactor)
    back(size * 0.05)


def flower():
    for i in range(6):
        fern(300, 10, 1)
        pencolor(i * 50 + 5, i * 50 + 5, i * 30 + 5)
        right(60)


init()
flower()
done()
