import turtle as t
import time

s = t.Screen()
s.tracer(10)


def shape(name, x, y):
    name.shapesize(x / 20, y / 20)


def lt():
    s.tracer(0)
    me.lt(90)
    s.tracer(10)


def rt():
    s.tracer(0)
    me.rt(90)
    s.tracer(10)


def is_collision_with(t1, t2):
    x1, y1 = t1.pos()
    x2, y2 = t2.pos()
    w1, h1 = t1.shapesize()[0] * 20, t1.shapesize()[1] * 20
    w2, h2 = t2.shapesize()[0] * 20, t2.shapesize()[1] * 20
    distance_y = abs(y1 - y2)
    distance_x = abs(x1 - x2)
    return distance_y < (w1 + w2) / 2 and distance_x < (h1 + h2) / 2


def up():
    s.tracer(0)
    old_pos = me.pos()
    lt()
    me.fd(10)
    if is_collision_with(me, bg1):
        me.setpos(old_pos)
        s.tracer(10)
    else:
        me.bk(10)
        s.tracer(10)
        me.fd(10)
    rt()


def down():
    s.tracer(0)
    old_pos = me.pos()
    rt()
    me.fd(10)
    if is_collision_with(me, bg1):
        me.setpos(old_pos)
        s.tracer(10)
    else:
        me.bk(10)
        s.tracer(10)
        me.fd(10)
    lt()


def right():
    s.tracer(0)
    old_pos = me.pos()
    me.fd(10)
    if is_collision_with(me, bg1):
        me.setpos(old_pos)
        s.tracer(10)
    else:
        me.bk(10)
        s.tracer(10)
        me.fd(10)


def left():
    s.tracer(0)
    old_pos = me.pos()
    me.bk(10)
    if is_collision_with(me, bg1):
        me.setpos(old_pos)
        s.tracer(10)
    else:
        me.fd(10)
        s.tracer(10)
        me.bk(10)


def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = me.pos()
    outside = x < left_wall or x > right_wall or y < bottom_wall or y > top_wall
    return outside


def game_over():
    t.bgcolor("green")
    t.clear()
    t.write("press space to start again", align="center", font=("Arial", 36, "normal"))


def win():
    right_wall = t.window_width() / 2
    x = me.xcor()
    return x > right_wall


def set_game_0():
    global bg1
    s.tracer(0)
    bg1 = t.Turtle()
    bg1.pu()
    bg1.shape("square")
    shape(bg1, 100, t.window_width())
    bg1.goto(0, -(t.window_height() / 2) + 50)
    bg1.color("white")
    s.tracer(10)


def distroy():
    i = 0
    while True:
        try:
            bg = "bg" + str(i)
            eval(bg).ht()
            i += 1
        except:
            return
        i += 1


def gravity():
    while not outside_window():
        time.sleep(0.01)
        down()


def game_start():
    global score
    t.clear()
    t.bgcolor("black")
    game_set = "set_game_" + str(score)
    try:
        eval(game_set)()
    except:
        t.write("you win", align="center", font=("Arial", 36, "normal"))
        score = 0
        return

    if win():
        t.bgcolor("green")
        t.write(
            "score: " + str(score) + "  press space to start another level",
            align="center",
            font=("Arial", 36, "normal"),
        )
    else:
        game_over()
    s.tracer(10)
    me.goto(0, 0)
    s.tracer(10)
    distroy()


me = t.Turtle()
me.shape("square")
me.color("green")
me.speed(5)
me.pu()
t.ht()
t.bgcolor("green")
t.write("press space to start", align="center", font=("Arial", 36, "normal"))
score = 0
t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onkey(game_start, "space")
t.listen()
t.mainloop()
