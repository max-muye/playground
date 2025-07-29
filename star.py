import turtle as t
import oval as o

t.speed(0)


def small_star(point, distance, color):
    t.color(color)
    t.begin_fill()
    for i in range(point):
        t.rt(360 / point)
        t.fd(distance)
        t.lt(720 / point)
        t.fd(distance)
    t.end_fill()


def planet(distance, color):
    t.color(color)
    t.begin_fill()
    t.circle(distance)
    t.end_fill()


def big_star(point, distance1, distance2, color):
    t.color(color)
    t.begin_fill()
    for i in range(point):
        t.rt(360 / point)
        t.fd(distance1)
        t.lt(720 / point)
        t.fd(distance1)
        t.rt(90 + 180 / point)
        t.fd(distance2)
        t.bk(distance2)
        t.lt(90 + 180 / point)
    t.end_fill()


def black_hole_(distance1, distance2, num):
    t.pensize(1)
    t.color("white")
    for i in range(num):
        t.pu()
        t.fd(distance1)
        t.lt(90)
        t.pd()
        t.circle(distance1)
        t.pu()
        t.rt(90)
        t.bk(distance1)
        t.pd()
        o.draw_oval(distance1 * 2, distance1 / 2)
        t.pu()
        t.fd(distance2)
        t.pd()


def neutron_star_(distance1, distance2, color):
    t.color(color)
    t.pu()
    t.fd(distance1)
    t.lt(90)
    t.pd()
    t.begin_fill()
    t.circle(distance1)
    t.end_fill()
    t.pu()
    t.rt(90)
    t.bk(distance1)
    t.pd()
    t.fd(distance2)
    t.bk(distance2 * 2)
    t.fd(distance2)


def supernova(point, distance, color):
    small_star(point, distance, color)
    big_star(point, distance, distance * 10, color)
    big_star(point, distance, distance * 10, "black")


def black_hole(distance1, distance2, distance3, point, num, color):
    supernova(point, distance1, color)
    black_hole_(distance2, distance3, num)


def neutron_star(distance1, distance2, distance3, point, color1, color2):
    supernova(point, distance1, color1)
    neutron_star_(distance2, distance3, color2)


def init():
    t.ht()
    t.speed(0)


def done():
    t.ht()
    t.done()
