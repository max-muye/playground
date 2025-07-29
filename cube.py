from all import *


class Cube:
    def __init__(
        self,
        size: int,
        fill=False,
        fillcolors=["red", "orange", "yellow", "green", "blue", "purple"],
        pencolor="black",
        color=None,
        pensize=2,
        x=0,
        y=0,
        z=0,
        show_how_to_command=True,
        set_onkeys=True,
        init_=True,
        init=True,
    ):
        if init:
            self.size = size
            self.points = []
            self.lines = []
            self.sides = []
            self.fill = fill
            self.fillcolors = fillcolors
            self.pencolor = pencolor
            self.color = color
            self.pensize = pensize
            if x != 0 or y != 0 or z != 0:
                z -= 0.3
            try:
                self.x = x * 0.2
            except:
                self.x = 0
                print("x is not a number")
            try:
                self.y = y * 0.2
            except:
                self.y = 0
                print("y is not a number")
            try:
                self.z = z * 0.2
            except:
                self.z = 0
                print("z is not a number")
            if init_:
                self.create_cube()
                self.draw()
                self.rotate()
                if set_onkeys:
                    self.on_key_press()
                    if show_how_to_command:
                        self.print_how_to_command()

    def create_cube(self):
        self.points = []
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    self.points.append((i, j, k))
        self.lines = [
            [self.points[0], self.points[1]],
            [self.points[1], self.points[3]],
            [self.points[3], self.points[2]],
            [self.points[2], self.points[0]],
            [self.points[4], self.points[5]],
            [self.points[5], self.points[7]],
            [self.points[7], self.points[6]],
            [self.points[6], self.points[4]],
            [self.points[0], self.points[4]],
            [self.points[1], self.points[5]],
            [self.points[3], self.points[7]],
            [self.points[2], self.points[6]],
        ]
        self.sides = [
            [self.points[0], self.points[1], self.points[3], self.points[2]],
            [self.points[4], self.points[5], self.points[7], self.points[6]],
            [self.points[0], self.points[4], self.points[5], self.points[1]],
            [self.points[1], self.points[5], self.points[7], self.points[3]],
            [self.points[3], self.points[7], self.points[6], self.points[2]],
            [self.points[2], self.points[6], self.points[4], self.points[0]],
        ]

    def project_3d_to_2d(self, x, y, z):
        scale = self.size
        angle = math.cos(math.pi / 4)
        screen_x = (x - y) * angle * scale
        screen_y = (x + y) * angle * 0.5 * scale - z * scale

        return screen_x, screen_y

    def rotate_x(self, angle):
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        new_lines = []
        for line in self.lines:
            new_line = []
            for point in line:
                x, y, z = point
                new_x = x - self.x
                new_y = (y - self.y) * cos_a - (z - self.z) * sin_a
                new_z = (y - self.y) * sin_a + (z - self.z) * cos_a
                new_line.append((new_x, new_y, new_z))
            new_lines.append(new_line)
        self.lines = new_lines
        new_sides = []
        for side in self.sides:
            new_side = []
            for point in side:
                x, y, z = point
                new_x = x - self.x
                new_y = (y - self.y) * cos_a - (z - self.z) * sin_a
                new_z = (y - self.y) * sin_a + (z - self.z) * cos_a
                new_side.append((new_x, new_y, new_z))
            new_sides.append(new_side)
        self.sides = new_sides

    def rotate_y(self, angle):
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        new_lines = []
        for line in self.lines:
            new_line = []
            for point in line:
                x, y, z = point
                new_x = (x - self.x) * cos_a + (z - self.z) * sin_a
                new_y = y - self.y
                new_z = -(x - self.x) * sin_a + (z - self.z) * cos_a
                new_line.append((new_x, new_y, new_z))
            new_lines.append(new_line)
        self.lines = new_lines
        new_sides = []
        for side in self.sides:
            new_side = []
            for point in side:
                x, y, z = point
                new_x = (x - self.x) * cos_a + (z - self.z) * sin_a
                new_y = y - self.y
                new_z = -(x - self.x) * sin_a + (z - self.z) * cos_a
                new_side.append((new_x, new_y, new_z))
            new_sides.append(new_side)
        self.sides = new_sides

    def rotate_z(self, angle):
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        new_lines = []
        for line in self.lines:
            new_line = []
            for point in line:
                x, y, z = point
                new_x = (x - self.x) * cos_a - (y - self.y) * sin_a
                new_y = (x - self.x) * sin_a + (y - self.y) * cos_a
                new_z = z - self.z
                new_line.append((new_x, new_y, new_z))
            new_lines.append(new_line)
        self.lines = new_lines
        new_sides = []
        for side in self.sides:
            new_side = []
            for point in side:
                x, y, z = point
                new_x = (x - self.x) * cos_a - (y - self.y) * sin_a
                new_y = (x - self.x) * sin_a + (y - self.y) * cos_a
                new_z = z - self.z
                new_side.append((new_x, new_y, new_z))
            new_sides.append(new_side)
        self.sides = new_sides

    def rotate(self, angles=0, xyzs="all", negative=False, angle=None):
        t.clear()
        if angle != None:
            angles = [angle] * 3
        if isinstance(angles, (int, float)):
            angles = [angles] * 3
        new_angles = []
        for angle in angles:
            new_angle = angle * math.pi / 180
            if negative:
                new_angles.append(-new_angle)
            else:
                new_angles.append(new_angle)
        if (xyzs == None or xyzs == "all") and len(angles) == 1:
            new_angles *= 3
        angles = new_angles
        if xyzs == None or xyzs == "all":
            xyzs = "xyz"
        for i, xyz in enumerate(list(xyzs)):
            eval("self.rotate_" + xyz + "(" + str(angles[i]) + ")")
        self.draw()

    def sort_sides(self):
        side_centers = []
        for side in self.sides:
            center_x = (side[0][0] + side[1][0] + side[2][0] + side[3][0]) / 4
            center_y = (side[0][1] + side[1][1] + side[2][1] + side[3][1]) / 4
            center_z = (side[0][2] + side[1][2] + side[2][2] + side[3][2]) / 4
            side_centers.append((center_x, center_y, center_z))

        side_depths = []
        for center in side_centers:
            center_x, center_y, center_z = center
            depth = center_x + center_y + center_z
            side_depths.append(depth)

        sorted_indices = sorted(
            range(len(side_depths)), key=lambda i: side_depths[i], reverse=True
        )

        new_sides = [self.sides[i] for i in sorted_indices]
        new_fillcolors = [self.fillcolors[i] for i in sorted_indices]
        self.sides = new_sides
        self.fillcolors = new_fillcolors

    def draw(
        self,
    ):
        xx, yy = t.pos()
        isdown = t.isdown()
        all_init(
            penup=True,
            speed=0,
            tracer=0,
            pencolor=self.pencolor,
            color=self.color,
            pensize=self.pensize,
            ht=True,
        )
        for line in self.lines:
            for i, point in enumerate(line):
                x, y, z = point
                _screen_x, _screen_y = self.project_3d_to_2d(x, y, z)
                screen_x, screen_y = self.project_3d_to_2d(self.x, self.y, self.z)
                screen_x = _screen_x + screen_x
                screen_y = _screen_y + screen_y

                if i == 0:
                    t.penup()
                    t.goto(screen_x, screen_y)
                    t.pendown()
                else:
                    t.goto(screen_x, screen_y)
                    t.penup()
        if self.fill:
            fillcolors = self.fillcolors.copy()
            for side in self.sides:
                self.sort_sides()
                if self.fillcolors != None:
                    t.fillcolor(fillcolors[0])
                    fillcolors.pop(0)
                for i, point in enumerate(side + [side[0]]):
                    x, y, z = point
                    _screen_x, _screen_y = self.project_3d_to_2d(x, y, z)
                    screen_x, screen_y = self.project_3d_to_2d(self.x, self.y, self.z)
                    screen_x = _screen_x + screen_x
                    screen_y = _screen_y + screen_y
                    if i == 0:
                        t.penup()
                        t.goto(screen_x, screen_y)
                        t.pendown()
                        t.begin_fill()
                    elif i == 4:
                        t.goto(screen_x, screen_y)
                        t.end_fill()
                        t.penup()
                    else:
                        t.goto(screen_x, screen_y)
        t.goto(xx, yy)
        if isdown:
            t.pendown()
        else:
            t.penup()
        s.update()

    def replace_draw(self):
        t.clear()
        self.__init__(
            self.size,
            x=self.x,
            y=self.y,
            z=self.z,
            fill=self.fill,
            fillcolors=self.fillcolors,
            pencolor=self.pencolor,
            color=self.color,
            pensize=self.pensize,
            show_how_to_command=False,
        )

    def handle_x(self):
        self.rotate(1, "x")

    def handle_X(self):
        self.rotate(1, "x", negative=True)

    def handle_y(self):
        self.rotate(1, "y")

    def handle_Y(self):
        self.rotate(1, "y", negative=True)

    def handle_z(self):
        self.rotate(1, "z")

    def handle_Z(self):
        self.rotate(1, "z", negative=True)

    def handle_c(self):
        self.replace_draw()

    def handle_r(self):
        self.rotate(1)

    def handle_R(self):
        self.rotate(1, negative=True)

    def handle_q(self):
        t.bye()

    def on_key_press(self):
        t.onkey(self.handle_x, "x")
        t.onkey(self.handle_X, "X")
        t.onkey(self.handle_y, "y")
        t.onkey(self.handle_Y, "Y")
        t.onkey(self.handle_z, "z")
        t.onkey(self.handle_Z, "Z")
        t.onkey(self.handle_c, "c")
        t.onkey(self.handle_r, "r")
        t.onkey(self.handle_R, "R")
        t.onkey(self.handle_q, "q")
        t.listen()

    def print_how_to_command(self):
        print("按以下键控制旋转：")
        print("x - 绕X轴旋转")
        print("y - 绕Y轴旋转")
        print("z - 绕Z轴旋转")
        print("反向旋转,按住shift键")
        print("r - 旋转立方体")
        print("c - 归位")
        print("q - 退出")
        print("-" * 50)

    def hide_turtle(self):
        t.ht()

    ht = hide_turtle


class Cubes:
    def __init__(self):
        self.c = Cube(0, init_=False)
        self.xyz_to_xy = self.c.project_3d_to_2d
        self.cube_count = 0
        self.cubes_xyz = []
        self.cubes = []
        self.cube_dict = {}

    def create_cube(
        self,
        xyz,
        size,
        rotate_angle=0,
        fill=False,
        fillcolors=["red", "orange", "yellow", "green", "blue", "purple"],
        pencolor="black",
        color=None,
        pensize=2,
    ):
        x, y, z = xyz
        name = "cube" + str(self.cube_count)
        things = (
            "Cube("
            + str(size)
            + ","
            + str(fill)
            + ","
            + str(fillcolors)
            + ","
            + '"'
            + str(pencolor)
            + '"'
            + ","
            + str(color)
            + ","
            + str(pensize)
            + ","
            + str(x)
            + ","
            + str(y)
            + ","
            + str(z)
            + ",set_onkeys=False)"
        )
        exec(name + "=" + things, globals())
        self.cubes_xyz.append((x, y, z))
        self.cubes.append(globals()[name])
        self.cube_count += 1
        eval(name).rotate(rotate_angle)

    def create_big_cube_shape(
        self,
        shape_size,
        size,
        xyz,
        pensize=2,
        colors=["red", "orange", "yellow", "green", "blue", "purple"],
    ):
        x, y, z = xyz
        shape_list = []
        if e.gll(colors) != 6:
            new_colors = []
            for i in colors:
                new_colors.append(
                    [[[i] for _ in range(shape_size)] for _ in range(shape_size)]
                )
            colors = new_colors

        shape_list = [
            [
                [["white" for _ in range(shape_size)] for _ in range(shape_size)]
                for _ in range(shape_size)
            ]
            for _ in range(6)
        ]
        for i, side_color in enumerate(colors):
            for j, line_color in enumerate(side_color):
                for k, color in enumerate(line_color):
                    shape_list[i][i][j][k] = color

        for i, colors in enumerate(shape_list):
            for j, colors in enumerate(colors):
                for k, colors in enumerate(colors):
                    self.create_cube(
                        xyz=[x + i * size, y + j * size, z + k * size],
                        size=size,
                        fill=True,
                        fillcolors=colors,
                        pensize=pensize,
                    )
    def draw_cubes(self):
        for cube in self.cubes:
            cube.draw()

    def mainloop(self):
        t.mainloop()


if __name__ == "__main__":
    size = 100
    c = Cubes()
    c.create_big_cube_shape(
        shape_size=2,
        xyz=[0, 0, 0],
        size=size,
        pensize=2,
    )
    c.draw_cubes()
    c.mainloop()
