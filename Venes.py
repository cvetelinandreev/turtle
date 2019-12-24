import turtle
import random
import sys
import tkinter


sys.setrecursionlimit(4000)

def getturtle():
    root = tkinter.Tk()
    root.tk.call('tk', 'scaling', 0.5)
    w = tkinter.Canvas(root, width=2000, height=1000)
    # root.geometry('2000x1500')  # added by me
    w.pack()
    screen = turtle.TurtleScreen(w)
    # screen.screensize(2000, 1500)  # added by me
    screen.tracer(0, 0)
    screen.colormode(255)

    initturtle = turtle.RawTurtle(screen)

    initturtle.reset();
    initturtle.pensize(4)
    initturtle.setheading(90)
    initturtle.penup()
    initturtle.goto(0, -200)

    return initturtle

def increment_green(turtle):
    currentcolor = turtle.pencolor()
    turtle.pencolor((int(currentcolor[0]), int(currentcolor[1] + 3) if currentcolor[1] < 250 else 250, int(currentcolor[2])))

def rotate(turtle, angle, direction):
    if direction == 'left':
        turtle.left(angle)
    elif direction == 'right':
        turtle.right(angle)

def spiral(spiralturtle, size, direction):
    if size < 0.1:
        return

    # rand = random.random();
    # probability_of_branching = 0.2
    # if (rand < probability_of_branching):
    #     newturtle = spiralturtle.clone()
    #
    #     #branch
    #     rotate(newturtle, 90, direction)
    #     sizeofbranch = size * 0.6
    #     spiral(newturtle, sizeofbranch, direction)
    #
    #     #flip for the next branch
    #     sizeafterbranching = size * 0.9
    #     if direction == 'left':
    #         spiral(spiralturtle, sizeafterbranching, 'right')
    #     elif direction == 'right':
    #         spiral(spiralturtle, sizeafterbranching, 'left')
    # else :
    spiralturtle.dot(size)

    spiralturtle.fd(size*0.4)

    # rotate(spiralturtle, 3, direction)
    spiral(spiralturtle, size*0.99, direction)


t = getturtle()
t.dot(300)
t.getscreen().mainloop()