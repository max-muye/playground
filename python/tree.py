import turtle as t

def init():
    t.left(90)
    t.speed(0)
    t.penup()
    t.backward(100)
    t.pendown()


# a=距离 b=角度 c=几及 d=被数 e=几个叉
def tree(a, b, c, d, e):
    t.forward(a)

    if c != 1:
        t.left(b)
        for i in range(e):
            tree(a * d, b, c - 1, d, e)
            t.right(b * 2 / (e - 1))
        t.left(b + b * 2 / (e - 1))

    t.backward(a)


init()
tree(100, 120, 5, 1, 5)
t.done()
