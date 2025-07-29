from tkinter import HIDDEN, NORMAL, Tk, Canvas


def toggle_eyes():
    current_color = c.itemcget(eye_left, "fill")
    new_color_eye = c.body_color if current_color == "white" else "white"
    new_color_pupil = c.body_color if current_color == "white" else "black"
    current_state = c.itemcget(mouth_normal, "state")
    new_state = HIDDEN if current_state == NORMAL else NORMAL
    c.itemconfigure(pupil_left, outline=new_color_pupil, fill=new_color_pupil)
    c.itemconfigure(pupil_right, outline=new_color_pupil, fill=new_color_pupil)
    c.itemconfigure(eye_left, outline=new_color_eye, fill=new_color_eye)
    c.itemconfigure(eye_right, outline=new_color_eye, fill=new_color_eye)


def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)


def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False


def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_main, state=NORMAL)
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.tongue_out = False


def show_happy(event):
    if 250 <= event.x <= 320 and 150 <= event.y <= 220:
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        if c.happy_level <= 10:
            c.happy_level += 1
    else:
        c.itemconfigure(cheek_left, state=HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)


def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(1000, sad)


def hide_happy(event):
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)


def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    c.itemconfigure(mouth_happy, state=NORMAL)
    c.itemconfigure(mouth_normal, state=HIDDEN)
    c.itemconfigure(mouth_sad, state=HIDDEN)
    c.happy_level += 1
    return


root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg="dark blue", highlightthickness=0)
c.body_color = "skyblue1"
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(
    75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color
)
ear_right = c.create_polygon(
    255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color
)

foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

eye_left = c.create_oval(130, 110, 160, 170, outline="black", fill="white")
pupil_left = c.create_oval(140, 145, 150, 155, outline="black", fill="black")
eye_right = c.create_oval(230, 110, 260, 170, outline="black", fill="white")
pupil_right = c.create_oval(240, 145, 250, 155, outline="black", fill="black")

mouth_normal = c.create_line(170, 250, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(
    170, 250, 200, 272, 230, 250, smooth=1, width=2, state=HIDDEN
)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
tongue_main = c.create_rectangle(
    170, 250, 230, 290, outline="red", fill="red", state=HIDDEN
)
tongue_tip = c.create_oval(170, 285, 230, 300, outline="red", fill="red", state=HIDDEN)

cheek_left = c.create_oval(70, 180, 120, 230, outline="pink", fill="pink", state=HIDDEN)
cheek_right = c.create_oval(
    280, 180, 330, 230, outline="pink", fill="pink", state=HIDDEN
)

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

root.after(1000, blink)
root.after(1000, sad)
c.pack()
c.bind("<Motion>", show_happy)
c.bind("<Leave>", hide_happy)
c.bind("<Double-1>", cheeky)
root.mainloop()
