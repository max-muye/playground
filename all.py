import 电路图 as dlt
import 竖式 as e
import sky as s
import turtle as t
import random as r
import time as ti
import tkinter as tk
import typing as tp
import math as m
import cube as c

电路图 = dlt
extra = e
sky = s
turtle = t
random = r
time = ti
tkinter = tk
typing = tp
cube = c
s = t.Screen()
screen = s
math = m
Turtle = t.Turtle()
Screen = t.Screen()


def hide_turtle():
    Turtle.ht()
    t.ht()


ht = hide_turtle


def all_init(
    type="turtle",
    bg=None,
    speed=None,
    penup=None,
    pencolor=None,
    fillcolor=None,
    color=None,
    pensize=None,
    tracer=None,
    ht=None,
):
    if type == "turtle":
        if bg != None:
            t.bgcolor(bg)
        if speed != None:
            t.speed(speed)
        if penup != None:
            t.penup()
        if pencolor != None and color == None:
            t.pencolor(pencolor)
        if fillcolor != None and color == None:
            t.fillcolor(fillcolor)
        if color != None and pencolor == None and fillcolor == None:
            t.color(color)
        if pensize != None:
            t.pensize(pensize)
        if tracer != None:
            s.tracer(tracer)
        if ht != False and ht != None:
            t.ht()


if __name__ == "__main__":
    pass
__name__ = ""
