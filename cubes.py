from all import *


def init():
    all_init(ht=False, speed=0)


# a=长度 b=正方体几级 c=正方体个数几级
def cubes(a, b, c, colors, color, x, y):
    def cube(a, b, colors, color):
        mark = []
        for i in range(3):
            if colors[i] != "no_color":
                t.color(colors[i])
                t.begin_fill()
            t.fd(a)
            t.rt(120)
            t.fd(a)
            t.rt(60)
            mark.append([round(t.xcor(), 6), round(t.ycor(), 6)])
            t.fd(a)
            t.rt(120)
            t.fd(a)
            t.lt(60)
            if colors[i] != "no_color":
                t.end_fill()

        t.color(color)

        for i in range(3):
            for i in range(b):
                t.fd(a / b)
                t.rt(120)
                t.fd(a)
                t.bk(a)
                t.lt(120)
            t.rt(120)
            for i in range(b):
                t.fd(a / b)
                t.rt(60)
                t.fd(a)
                t.bk(a)
                t.lt(60)
            t.rt(60)
            t.fd(a)
            t.rt(120)
            t.fd(a)
            t.lt(60)
        return mark

    has_mark = []
    has_not_mark = [[x, y]]
    for i in range(c):
        if i % 2 == 1:
            t.lt(60)
            now_colors = colors[:3]
        else:
            now_colors = colors[:3]
        marks = []
        while has_not_mark:
            now_XY = has_not_mark.pop()
            has_mark.append(now_XY)
            t.penup()
            t.goto(now_XY[0], now_XY[1])
            t.pendown()
            for j in cube(a, b, now_colors, color):
                if j not in has_mark and j not in marks:
                    marks.append(j)
        has_not_mark = marks[:]
        if i % 2 == 1:
            t.rt(60)


def done():
    t.done()


if __name__ == "__main__":
    cubes(
        500,
        100,
        5,
        ["white", "yellow", "red", "orange", "blue", "green"],
        "black",
        0,
        0,
    )
    done()
