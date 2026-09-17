""" import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
def rectangle(x):
    t.forward(x + 25)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x + 25)
    t.left(90)
    t.forward(x)
rectangle(100)


turtle.done() """


""" import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(90)


turtle.done() """



""" import turtle
from turtle import *
t = Turtle()

for i in range(60):
    def square(x):
        for i in range(4):
            t.forward(x)
            t.left(90)
        t.left(5)
       
    square(200) """

""" import turtle
from turtle import *
t = Turtle()

t.shape("turtle")

def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
        t.right(5)
addSquares(60)

turtle.done() """

""" import turtle
from turtle import *
t = Turtle()

t.shape("turtle")

def shape(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
def addshape(iRange):
    length = 5
    for i in range(iRange):
        shape(length, 144)
        length += 5
        t.right(5)
addshape(60)

turtle.done() """