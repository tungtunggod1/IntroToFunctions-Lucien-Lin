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

import turtle
from turtle import *
t = Turtle()

def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        doubleSquares(length, 90)
        length = length * 2
doubleSquares(5)

