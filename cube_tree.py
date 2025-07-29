from all import *


def init():
    all_init(ht=False, speed=0)


# a=距离 b=角度 c=几及 d=被数 e=几个叉 f=e
def cube_tree(a, c, d, e, f):
    t.setheading(90)
    b = 180
    if c != f:
        t.pu()
        t.forward(a)
        t.pd()
    if e % 3 == 0 or c != f:
        mark = [round(t.xcor(), 6), round(t.ycor(), 6)]
        cubes.cubes(a / c, 1, c, ["no_color"] * 6, "black", mark[0], mark[1])
        t.pu()
        t.goto(mark[0], mark[1])
        t.pd()

    if c != 1:
        mark_heading = t.heading()
        t.left(b)
        for i in range(e):
            cube_tree(a * d, b, c - 1, d, e, f)
            t.right(b * 2 / e)
        t.setheading(mark_heading)

    t.pu()
    t.backward(a)
    t.pd()
    return "ok"


if __name__ == "__main__":
    init()
    cube_tree(50, 5, 1, 3, 5)
    cubes.done()
