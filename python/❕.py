import turtle as t

t.pensize(10)
t.speed(5)
for i in range(3):
    t.forward(200)
    t.left(120)

t.left(90)
t.pensize(20)
t.penup()
t.goto(100, 30)
t.pendown()
t.forward(1)
t.penup()
t.forward(30)
t.pendown()
t.forward(50)
t.hideturtle()
t.done()
