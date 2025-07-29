from all import *

import turtle as t


def set_things():
    global gates, lines, in_, pd, out_, points, input_list, lights, in_list, out_list, in_out, s
    gates = {}
    lines = {}
    in_ = ()
    pd = True
    out_ = None
    points = {}
    input_list = []
    lights = {}
    in_list = []
    out_list = []
    in_out = {}
    s = t.Screen()


def up():
    global pd
    pd = False
    t.pu()


def down():
    global pd
    global points
    pd = True
    t.pd()
    x, y = t.pos()
    x = round(x)
    y = round(y)
    try:
        points.pop((x, y))
    except:
        pass
    points.update({(x, y): False})


def lt():
    s.tracer(0)
    t.lt(90)
    s.tracer(1)


def rt():
    s.tracer(0)
    t.rt(90)
    s.tracer(1)


def fd():
    global pd
    global lines
    global points
    s.tracer(0)
    x, y = t.pos()
    x = round(x)
    y = round(y)
    t.fd(10)
    x2, y2 = t.pos()
    x2 = round(x2)
    y2 = round(y2)
    if pd:
        try:
            lines.pop(((x, y), (x2, y2)))
        except:
            pass
        try:
            lines.pop(((x2, y2), (x, y)))
        except:
            pass
        try:
            points.pop((x, y))
        except:
            pass
        lines.update({((x, y), (x2, y2)): False})
        lines.update({((x2, y2), (x, y)): False})
        points.update({(x2, y2): False})
    s.tracer(1)


def clear():
    global gates, lines, in_, input_list, pd, out_, points, lights, in_list, out_list, in_out
    s.tracer(0)
    t.goto(0, 0)
    t.seth(0)
    t.clear()
    t.pd()
    s.tracer(1)

    set_things()


def _in():
    global in_
    x, y = t.pos()
    x = round(x)
    y = round(y)
    in_ = in_ + ((x, y),)
    t.dot(10)


def _out():
    global out_
    x, y = t.pos()
    x = round(x)
    y = round(y)
    out_ = (x, y)
    t.dot(10)


def set_input_0():
    global points, input_list
    x, y = t.pos()
    x = round(x)
    y = round(y)
    try:
        points.pop((x, y))
    except:
        pass

    points.update({(x, y): False})
    input_list.append((x, y))
    input_list = list(set(input_list))
    run("all", tf=False, now_runing=input_list)


def set_input_1():
    global points, input_list
    x, y = t.pos()
    x = round(x)
    y = round(y)
    try:
        points.pop((x, y))
    except:
        pass
    points.update({(x, y): True})
    try:
        input_list.append((x, y))
    except:
        pass
    input_list = list(set(input_list))
    run("all", tf=True, now_runing=input_list)


def draw_gate(gate_type):
    x, y = t.pos()
    x = round(x)
    y = round(y)
    xy = (x, y)
    global in_, out_, in_list, out_list
    s.tracer(0)
    in__ = in_[:]

    # 检查输入点是否对齐，并确定绘制参数
    if gate_type != "not":
        if in_[0][0] == in_[1][0]:  # 垂直对齐
            x = in_[0][0]
            coordinates = tuple(point[1] for point in in_)  # y坐标
            is_vertical = True
        elif in_[0][1] == in_[1][1]:  # 水平对齐
            y = in_[0][1]
            coordinates = tuple(point[0] for point in in_)  # x坐标
            is_vertical = False
        else:
            t.write("输入点不一致")
            clear()
            s.tracer(1)
            return

    # 设置门的颜色
    if gate_type == "not":
        t.color("red")
    elif gate_type == "or":
        t.color("yellow")
    elif gate_type == "and":
        t.color("blue")
    else:
        t.write("门类型错误")
        clear()
        s.tracer(1)
        return

    # 绘制门的形状
    t.goto(out_[0], out_[1])
    t.begin_fill()
    if gate_type == "not":
        t.goto(in_[0][0], in_[0][1])
        t.dot(10)
        t.goto(out_[0], out_[1])
        t.dot(10)
    elif is_vertical:  # 垂直对齐
        t.goto(x, max(coordinates))
        t.goto(x, min(coordinates))
    else:  # 水平对齐
        t.goto(max(coordinates), y)
        t.goto(min(coordinates), y)
    t.goto(out_[0], out_[1])
    t.dot(10)
    t.end_fill()

    # 绘制输入点
    s.tracer(0)
    for i in in__:
        t.goto(i[0], i[1])
        t.dot(10)
    t.color("black")

    # 保存门的信息（使用原始的坐标对）
    gate_inputs = in__[:]  # 保留完整的输入坐标对
    try:
        gates.pop((tuple(gate_inputs), out_))
    except:
        pass
    try:
        gates.pop((out_, tuple(gate_inputs)))
    except:
        pass
    gates.update({(tuple(gate_inputs), out_): gate_type})
    gates.update({(out_, tuple(gate_inputs)): gate_type})
    in_list = list(set(in_list))
    in_list.append(tuple(gate_inputs))
    out_list = list(set(out_list))
    out_list.append(out_)
    try:
        in_out.pop(tuple(gate_inputs))
    except:
        pass
    try:
        in_out.pop(out_)
    except:
        pass
    in_out.update({tuple(gate_inputs): out_})
    in_out.update({out_: tuple(gate_inputs)})

    # 重置in_
    in_ = ()
    s.tracer(0)
    t.goto(xy[0], xy[1])
    s.tracer(1)


def not_gate():
    draw_gate("not")


def or_gate():
    draw_gate("or")


def and_gate():
    draw_gate("and")


def set_light(tf=False):
    x, y = t.pos()
    x = round(x)
    y = round(y)
    s.tracer(0)
    t.color("green" if tf else "red")  # 设置灯为红色,代表没有通电
    t.begin_fill()
    t.pu()
    t.fd(5)
    t.pd()
    t.lt(90)
    t.fd(5)
    for i in range(3):
        t.lt(90)
        t.fd(10)
    t.lt(90)
    t.fd(5)
    t.lt(90)
    t.pu()
    t.fd(5)
    t.pd()
    t.rt(180)
    s.tracer(1)
    lights.update({(x, y): tf})
    t.end_fill()


def update(
    type,
    x1,
    y1,
    tf=None,
    x2=None,
    y2=None,
    gate_xy_list=None,
    gate_type=None,
):
    try:
        s.tracer(0)
        global gates, lines, points, lights

        if type == "line":
            lines.pop(((x1, y1), (x2, y2)))
            lines.pop(((x2, y2), (x1, y1)))
            lines.update({((x1, y1), (x2, y2)): tf})
            lines.update({((x2, y2), (x1, y1)): tf})
            t.color("green" if tf else "red")
            t.pu()
            t.goto(x1, y1)
            t.pd()
            t.goto(x2, y2)
            t.pu()
        elif type == "point":
            points.pop((x1, y1))
            points.update({(x1, y1): tf})
        elif type == "gate":
            gate_TF_list = []
            for i in gate_xy_list:
                gate_TF_list.append(points[i])
            gate_TF_list = list(set(gate_TF_list))
            ret = False
            if gate_type == "not":
                ret = not gate_TF_list[0]
            elif gate_type == "or":
                for i in gate_TF_list:
                    ret = ret or i
            elif gate_type == "and":
                ret = True
                for i in gate_TF_list:
                    ret = ret and i
            points.pop((x1, y1))
            points.update({(x1, y1): ret})
            run("all")
        elif type == "light":
            t.goto(x1, y1)
            lights.pop((x1, y1))
            set_light(tf)
        s.tracer(1)
        return True
    except:
        return False


def find_line(x, y):
    global lines
    lines_list = list(lines)
    res = []
    for i in lines_list:
        if (x, y) == i[0]:
            res.append(i[1])
        elif (x, y) == i[1]:
            res.append(i[0])
    res = list(set(res))
    return res


def run(type, x1=None, y1=None, tf=None, none_line=None, now_runing=None):
    global gates, lines, points, input_list, lights, in_list, out_list, in_out
    if now_runing is None:
        now_runing = input_list.copy()
    if type == "all":
        now = []
        xy_list = []
        for i in now_runing:
            for j, k in gates.items():
                if i in j:
                    run("gate", in_out[j[0]][0], in_out[j[0]][1])
            xy = tuple(run("line", i[0], i[1], tf))
            xy_list.append(xy)
            xy_list = list(set(xy_list))
            for j in list(gates):
                if xy in j[0]:
                    now.append(j[1])
            now = list(set(now))
        if now:
            run("all", now_runing=now)
        else:
            for i in xy_list:
                run("output", i[0], i[1])
    elif type == "line":
        fl = find_line(x1, y1)
        if none_line:
            fl.remove(none_line)
        if fl:
            res = []
            for i in fl:
                run("output", i[0], i[1])
                lines.update({((x1, y1), i): tf})
                lines.update({(i, (x1, y1)): tf})
                points.update({i: tf})
                update("line", x1, y1, tf, i[0], i[1])
                update("point", i[0], i[1], tf)
                res += run("line", i[0], i[1], tf, none_line=(x1, y1))
            return res
        else:
            return (x1, y1)
    elif type == "gate":
        in_ = in_out[(x1, y1)]
        gate_type = gates[(in_, (x1, y1))]
        update("gate", x1, y1, gate_type=gate_type, gate_xy_list=list(in_))
    elif type == "output":
        update("light", x1, y1)


def try_run():
    global gates, lines, points, input_list, lights, in_list, out_list, in_out
    print()
    print(gates)
    print(lines)
    print(points)
    print(input_list)
    print(lights)
    print(in_list)
    print(out_list)
    print(in_out)


def set_key():
    t.onkey(up, "Up")
    t.onkey(down, "Down")
    t.onkey(lt, "Left")
    t.onkey(rt, "Right")
    t.onkey(fd, "space")
    t.onkey(clear, "c")
    t.onkey(not_gate, "n")
    t.onkey(or_gate, "o")
    t.onkey(and_gate, "a")
    t.onkey(set_input_0, "0")
    t.onkey(set_input_1, "1")
    t.onkey(_in, "i")
    t.onkey(_out, "u")
    t.onkey(set_light, "l")
    t.onkey(try_run, "t")


def main():
    t.color("red")
    global s
    set_things()
    set_key()
    t.listen()
    t.mainloop()


if __name__ == "__main__":
    main()
# 441
