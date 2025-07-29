from all import *


def init():
    t.write("press space to start 2048", align="center", font=("Arial", 40, "bold"))


def move_one_left(turtle_):
    global length
    turtle_.fd(-length)


def move_one_right(turtle_):
    global length
    turtle_.fd(length)


def move_one_up(turtle_):
    global length
    turtle_.lt(90)
    turtle_.fd(length)
    turtle_.rt(90)


def move_one_down(turtle_):
    global length
    turtle_.rt(90)
    turtle_.fd(-length)
    turtle_.lt(90)


def set_one_turtle():
    global main_list, num
    i, j = r.randint(0, num - 1), r.randint(0, num - 1)
    while main_list[i][j][0] != 0:
        i, j = r.randint(0, num - 1), r.randint(0, num - 1)
    main_list[i][j][0] = 1


def two_turtles_to_one(turtle1, turtle2, direction):
    global main_list, num, length
    x1, y1 = turtle1.pos()
    x2, y2 = turtle2.pos()
    mark = turtle2.pos()
    x1, y1, x2, y2 = x1 // length, y1 // length, x2 // length, y2 // length
    s.tracer(1)
    eval("move_one_" + direction)(turtle2)
    s.tracer(0)
    main_list[x1][y1][0] *= 2
    main_list[x2][y2][0] = 0
    turtle2.ht()
    s.tracer(0)
    turtle2.goto(mark[0], mark[1])
    turtle2.st()


def move_turtles_left():
    global main_list, num, length
    set_color_right()
    for i in range(num):
        for j in range(num):
            flag = False
            k = 1
            while main_list[i][j - k][0] == 0:
                k += 1
                try:
                    if main_list[i][j - k][0]:
                        flag = True
                        break
                except:
                    break
            if not flag:
                break
            else:
                two_turtles_to_one(main_list[i][j][1], main_list[i][j - k][1], "left")
    set_one_turtle()
    set_color_right()


def move_turtles_right():
    global main_list, num, length
    set_color_right()
    for i in range(num):
        for j in range(num):
            flag = False
            k = 1
            while main_list[i][j + k][0] == 0:
                k += 1
                try:
                    if main_list[i][j + k][0]:
                        flag = True
                        break
                except:
                    break
            if not flag:
                break
            else:
                two_turtles_to_one(main_list[i][j][1], main_list[i][j + k][1], "right")
    set_one_turtle()
    set_color_right()


def move_turtles_up():
    global main_list, num, length
    set_color_right()
    for i in range(num):
        for j in range(num):
            flag = False
            k = 1
            while main_list[i - k][j][0] == 0:
                k += 1
                try:
                    if main_list[i - k][j][0]:
                        flag = True
                        break
                except:
                    break
            if not flag:
                break
            else:
                two_turtles_to_one(main_list[i][j][1], main_list[i - k][j][1], "up")
    set_one_turtle()
    set_color_right()


def move_turtles_down():
    global main_list, num, length
    set_color_right()
    for i in range(num):
        for j in range(num):
            flag = False
            k = 1
            try:
                tf = bool(main_list[i + k][j][0])
            except:
                continue
            while tf == 0:
                k += 1
                if tf:
                    flag = True
                    break
            if not flag:
                break
            else:
                two_turtles_to_one(main_list[i][j][1], main_list[i + k][j][1], "down")
    set_one_turtle()
    set_color_right()


def set_onkey_press():
    t.onkey(move_turtles_left, "Left")
    t.onkey(move_turtles_right, "Right")
    t.onkey(move_turtles_up, "Up")
    t.onkey(move_turtles_down, "Down")
    t.onkey(t.bye, "q")
    t.onkey(main_, "space")
    t.listen()


def set_color_right():
    global main_list
    for i in main_list:
        for j in i:
            k = [int(x) for x in ["0", "0"] + list(str(j[0]))]
            j[1].color(k[0], k[1], k[2])


def main_(num_=4, length_=100):
    global main_list, num, length
    t.clear()
    main_list = [[[0, None] for _ in range(num_)] for _ in range(num_)]
    turtle_count = 0
    length = length_
    num = num_
    s.tracer(0)
    x = -t.window_width() / 2 + length / 2
    y = -t.window_height() / 2 + length / 2
    for i in range(num):
        for j in range(num):
            name = "t" + str(turtle_count)
            exec(name + "=t.Turtle()", globals())
            turtle_count += 1
            name = eval(name)
            main_list[i][j][1] = name
            name.shape("square")
            name.shapesize(length / 20)
            name.color("red")
            name.penup()
            name.goto(x + i * length, y + j * length)
    set_one_turtle()
    set_color_right()
    while False:
        set_color_right()
        time.sleep(0.01)


def main():
    t.ht()
    t.fd(0)
    init()
    set_onkey_press()
    t.mainloop()


if __name__ == "__main__":
    main()
