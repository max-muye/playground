import turtle as t
import math

def draw_oval(width, height):
    t.pensize(2)
    # 保存当前位置和朝向
    start_x = t.xcor()
    start_y = t.ycor()
    heading = t.heading()
    
    # 使用参数方程绘制椭圆
    t.penup()
    steps = 360  # 步数越多，椭圆越平滑
    for angle in range(steps):
        rad = math.radians(angle)
        x = width * math.cos(rad)
        y = height * math.sin(rad)
        t.goto(start_x + x, start_y + y)
        if angle == 0:
            t.pendown()
    
    # 回到起点并恢复朝向
    t.penup()
    t.goto(start_x, start_y)
    t.seth(heading)
    t.pendown()

# 使用示例
# t.speed(0)
# draw_oval_2(100, 50)  # 宽200，高100的椭圆
# t.done()