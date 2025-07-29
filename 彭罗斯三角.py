import turtle as t

msg = 3

a = 360 / msg
b = 180 - a

t.speed(0)

for i in range(msg):
    rainbow_colors = ["#FF0000", "#FF7F00", "#FFFF00"]
    color_index = i % len(rainbow_colors)
    t.color(rainbow_colors[color_index])
    t.begin_fill()

    t.forward(100)
    t.left(a)
    t.forward(200)
    t.right(a)
    t.forward(50)
    t.right(b)
    t.forward(250)
    t.right(a)
    t.forward(200)
    t.right(a)
    t.forward(50)
    t.end_fill()
    t.forward(50)
    t.right(180)

t.hideturtle()
t.done()
