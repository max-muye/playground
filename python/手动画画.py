from all import *


def fd():
    _.fd(10)


def bk():
    _.bk(10)


def lt():
    _.lt(10)


def rt():
    _.rt(10)


def big_fd():
    _.fd(100)


def big_bk():
    _.bk(100)


def big_lt():
    _.lt(90)


def big_rt():
    _.rt(90)


def up():
    _.pu()


def down():
    _.pd()


def e():
    global color
    _.color("white")
    color = "white"


def b():
    global color
    _.color("blue")
    color = "blue"


def r():
    global color
    _.color("red")
    color = "red"


def g():
    global color
    _.color("green")
    color = "green"


def y():
    global color
    _.color("yellow")
    color = "yellow"


def p():
    global color
    _.color("purple")
    color = "purple"


def o():
    global color
    _.color("orange")
    color = "orange"


def bg():
    t.bgcolor(color)


def be():
    _.begin_fill()


def en():
    _.end_fill()


def star():
    for i in range(5):
        _.fd(100)
        _.rt(144)


def circle():
    _.circle(100)


def square():
    for i in range(4):
        _.fd(100)
        _.rt(90)


def triangle():
    for i in range(3):
        _.fd(100)
        _.rt(120)


def rectangle():
    for i in range(2):
        _.fd(100)
        _.rt(90)
        _.fd(50)
        _.rt(90)


def heart():
    _.circle(50, 180)
    _.circle(100, 180)
    _.circle(50, 180)


def c():
    global color
    _.clear()
    _.reset()
    _.pu()
    _.goto(0, 0)
    _.pd()
    color = "black"
    t.bgcolor("white")


_ = Turtle
_.shape("square")
c()
t.onkey(fd, "Up")
t.onkey(bk, "Down")
t.onkey(lt, "Left")
t.onkey(rt, "Right")
t.onkey(up, "w")
t.onkey(down, "s")
t.onkey(e, "e")
t.onkey(c, "c")
t.onkey(b, "b")
t.onkey(r, "r")
t.onkey(g, "g")
t.onkey(y, "y")
t.onkey(p, "p")
t.onkey(o, "o")
t.onkey(be, "1")
t.onkey(en, "2")
t.onkey(big_lt, "9")
t.onkey(big_rt, "0")
t.onkey(big_fd, "/")
t.onkey(big_bk, "\\")
t.onkey(star, "3")
t.onkey(circle, "4")
t.onkey(square, "5")
t.onkey(triangle, "6")
t.onkey(rectangle, "7")
t.onkey(heart, "8")
t.onkey(bg, "space")
t.listen()
t.mainloop()
