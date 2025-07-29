import turtle as t

t.pencolor("white")
t.speed(0)
t.goto(-700, -400)

# a=距离 b=个数 c=几边形
def o(a, b, c):
    d = a
    for i in range(b):
        d /= 2
    if a<=d:
        t.fillcolor("green")
        t.begin_fill()
    for i in range(c):
        t.forward(a)
        t.left(360 / c)
        if a > d:
            o(a / 2, b - 1, c)
    if a<=d:
        t.end_fill()
o(900,3, 3)
t.done()
