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


import turtle
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


turtle.done()