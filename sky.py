import star as s
import random as r
import turtle as t
import extra as e

sn = t.Screen()


def draw_star(x=None, y=None):
    if x != None and y != None:
        t.goto(x, y)
    else:
        t.goto(r.randint(-700, 700), r.randint(-400, 400))
    random_num = r.randint(1, 11111)
    if random_num <= 10000:
        small_star()
    elif random_num <= 11000:
        planet()
    elif random_num <= 11100:
        big_star()
    elif random_num <= 11110:
        neutron_star()
    elif random_num <= 11111:
        black_hole()


def small_star(x=None, y=None):
    sn.tracer(0)
    isdown = t.isdown()
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.small_star(
        r.randint(4, 10),
        r.uniform(3, 4),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    sn.tracer(1)
    if isdown:
        t.pendown()
    else:
        t.penup()


def planet(x=None, y=None):
    isdown = t.isdown()
    sn.tracer(0)
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.planet(
        r.uniform(10, 20),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    sn.tracer(1)
    if isdown:
        t.pendown()
    else:
        t.penup()


def big_star(x=None, y=None):
    isdown = t.isdown()
    sn.tracer(0)
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.big_star(
        r.randint(4, 10),
        r.uniform(10, 20),
        r.uniform(10, 20),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    sn.tracer(1)
    if isdown:
        t.pendown()
    else:
        t.penup()


def neutron_star(x=None, y=None):
    isdown = t.isdown()
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.neutron_star(
        r.uniform(10, 20),
        r.uniform(10, 20),
        r.uniform(100, 200),
        r.randint(4, 10),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    if isdown:
        t.pendown()
    else:
        t.penup()


def black_hole(x=None, y=None):
    isdown = t.isdown()
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.black_hole(
        r.uniform(10, 20),
        r.uniform(50, 60),
        r.uniform(1, 5),
        r.randint(4, 10),
        r.randint(1, 10),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    if isdown:
        t.pendown()
    else:
        t.penup()


def neutron_star_(x=None, y=None):
    isdown = t.isdown()
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.neutron_star_(
        r.uniform(10, 20),
        r.uniform(100, 200),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    if isdown:
        t.pendown()
    else:
        t.penup()


def black_hole_(x=None, y=None):
    isdown = t.isdown()
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.black_hole_(r.uniform(50, 60), r.uniform(1, 5), r.randint(1, 10))
    if isdown:
        t.pendown()
    else:
        t.penup()


def supernova(x=None, y=None):
    isdown = t.isdown()
    if x != None and y != None:
        t.goto(x, y)
    t.pendown()
    s.supernova(
        r.randint(4, 10),
        r.uniform(10, 20),
        (r.uniform(0.75, 1), r.uniform(0.75, 1), r.uniform(0.75, 1)),
    )
    if isdown:
        t.pendown()
    else:
        t.penup()


def draw_sky(
    tf="",
    num=0,
    xy_list=None,
    shape=None,
    shape_length=101,
    shape_type="planet",
    click_tf=False,
    random_click=None,
):
    t.bgcolor("black")
    s.init()
    t.pensize(1)
    if click_tf:

        def clear():
            t.clearscreen()
            init()
            draw_sky(tf, num, xy_list, click_tf, random_click)

        if random_click == None:
            random_click = True
        if random_click:
            while True:
                t.onscreenclick(lambda x, y: draw_star(x, y))
                t.onkey(t.penup, "Up")
                t.onkey(t.pendown, "Down")
                t.onkey(clear, "c")
                t.listen()
                t.mainloop()  # 等待点击事件
        else:

            def click_small_star():
                t.onscreenclick(lambda x, y: small_star(x, y))

            def click_planet():
                t.onscreenclick(lambda x, y: planet(x, y))

            def click_big_star():
                t.onscreenclick(lambda x, y: big_star(x, y))

            def click_neutron_star():
                t.onscreenclick(lambda x, y: neutron_star(x, y))

            def click_black_hole():
                t.onscreenclick(lambda x, y: black_hole(x, y))

            while True:
                t.onkey(click_small_star, "s")
                t.onkey(click_planet, "p")
                t.onkey(click_big_star, "b")
                t.onkey(click_neutron_star, "n")
                t.onkey(click_black_hole, "space")
                t.onkey(t.penup, "Up")
                t.onkey(t.pendown, "Down")
                t.onkey(clear, "c")
                t.listen()
                t.mainloop()  # 等待点击事件
    else:
        t.penup()
        sn.tracer(0)
        if xy_list or shape:
            if shape:
                xy_list = e.fi(e.ep(shape, shape_length, print_TF=False), "#", 2)
            for xy in xy_list:
                eval(shape_type)(xy[1] - 700, shape_length - xy[0])
            sn.update()
        elif tf == "":
            if input("是否画无限颗星星(y/n):") == "n":
                for i in range(int(input("请输入个数:"))):
                    draw_star()
                    sn.update()
            else:
                while True:
                    draw_star()
                    sn.update()
        elif tf:
            while True:
                draw_star()
                sn.update()
        else:
            for i in range(num):
                draw_star()
                sn.update()

    s.done()


def show():
    small_star()
    planet()
    big_star()
    neutron_star()
    black_hole()


def show_sky():
    show()
    draw_sky()


def init():
    s.init()
    t.pensize(1)
    t.bgcolor("black")


def done():
    s.done()


if __name__ == "__main__":
    draw_sky()
