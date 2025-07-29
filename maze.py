import turtle as t


def is_collision(t1, t2):
    if t1.xcor() == t2.xcor() and t1.ycor() == t2.ycor():
        return True
    return False


def draw_maze(x, y):
    me.shapesize(600 / x / 20, 600 / y / 20)
    me.pensize(600 / x)
    s.tracer(0)
    me.pu()
    me.goto(
        t.window_width() / 2 - 600 / x * 1.5, -t.window_height() / 2 + 600 / y * 2.5
    )
    me.pd()
    me.fd(0)
    me.pu()
    me.goto(
        -t.window_width() / 2 + 600 / x * 0.75, t.window_height() / 2 - 600 / y * 1.5
    )
    me.pd()
    me.fd(0)
    s.tracer(1)


s = t.Screen()
s.bgcolor("black")
s.title("Maze")
s.setup(600, 600)
me = t.Turtle()
me.shape("circle")
me.color("white")
me.pu()
me.goto(0, 0)
me.color("white")
draw_maze(50, 50)
t.done()
