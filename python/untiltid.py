import turtle as t

t.speed(0)
t.left(135)
a = 6
b = 4
for i in range(a):
    for i in range(b):
        t.forward(30)
        t.right(360 / b)
    t.right(360 / a)
t.done()
