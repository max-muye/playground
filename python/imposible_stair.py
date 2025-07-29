import turtle as t
import cubes as c

def init():
    t.ht()
    t.speed(0)


# a= 长度 xb= x级数 yb= y级数 colors= 填充颜色 color=颜色
def imposible_stair(a, xb, yb, colors, color, x, y):
    if xb < 4 or yb < 3:
        return "级数不能小于4和3"
    for i in range(0, a * xb, a):
        c.cubes(a, 1, 1, colors, color, i + x, y)
    for i in range(0, a * yb, a):
        c.cubes(a, 1, 1, colors, color, a * xb - a + x, i + y)
    for i in range(a * xb - a, -a, -a):
        c.cubes(a, 1, 1, colors, color, i + x, a * yb - a + y)
    for i in range(a * yb - a, -a, -a):
        c.cubes(a, 1, 1, colors, color, x, i + y)
    for i in range(0, a + a, a):
        c.cubes(a, 1, 1, colors, color, i + x, y)
    t.fillcolor(colors[-1])
    t.begin_fill()
    t.lt(60)
    t.fd(a)
    t.rt(120)
    t.fd(a)
    t.rt(60)
    t.fd(a)
    t.rt(120)
    t.fd(a)
    t.end_fill()
    return "完成"


def done():
    t.done()


# init()
# imposible_stair(10,30, 10, ["red", "yellow", "blue"], "black", -350, -350)
# done()
