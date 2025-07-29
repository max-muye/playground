from itertools import cycle
from random import randrange
from tkinter import Canvas, PhotoImage, Tk, messagebox, font, messagebox
import random
from PIL import Image, ImageTk
import pygame

pygame.mixer.init()
catch_sound = pygame.mixer.Sound("sounds/mixkit-winning-a-coin-video-game-2069.wav")
broken_sound = pygame.mixer.Sound("sounds/mixkit-glass-break-with-hammer-thud-759.wav")
try:
    pygame.mixer.music.load("sounds/game-music-loop-7-145285.wav")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
except Exception as e:
    print(f"无法加载背景音乐: {e}")

canvas_width = 800
canvas_height = 400
root = Tk()
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue")

try:
    image = Image.open("background.jpeg")
    image = image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
    background_image = ImageTk.PhotoImage(image)
    background = c.create_image(0, 0, image=background_image, anchor="nw")
    root.background_image = background_image  # 防止图片被垃圾回收
except Exception as e:
    print(f"无法加载背景图片: {e}")
    c.configure(background="deep sky blue")  # 如果加载失败，使用纯色背景

# c.create_rectangle(
#     -5,
#     canvas_height - 100,
#     canvas_width + 5,
#     canvas_height + 5,
#     fill="sea green",
#     width=0,
# )

c.create_oval(-80, -80, 120, 120, fill="orange", width=0)
c.pack()

color_cycle = cycle(
    ["light blue", "light green", "light pink", "light yellow", "light cyan"]
)
egg_width = 45
egg_height = 55
egg_score = 1
egg_speed = 500
egg_interval = 4000
difficulty_factor = 0.99

catcher_color = "blue"
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width / 2 - catcher_width / 2
catcher_start_y = canvas_height - catcher_height - 20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher = c.create_arc(
    catcher_start_x,
    catcher_start_y,
    catcher_start_x2,
    catcher_start_y2,
    start=200,
    extent=140,
    style="arc",
    outline=catcher_color,
    width=3,
)
catcher_color = "red"
catcher2 = c.create_arc(
    catcher_start_x,
    catcher_start_y,
    catcher_start_x2,
    catcher_start_y2,
    start=200,
    extent=140,
    style="arc",
    outline=catcher_color,
    width=3,
)

game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)

score = 0
score2 = 0
score_text = c.create_text(
    10,
    10,
    anchor="nw",
    font=game_font,
    fill="darkblue",
    text="Score: " + str(score),
)
score_text2 = c.create_text(
    10,
    30,
    anchor="nw",
    font=game_font,
    fill="darkred",
    text="Score: " + str(score2),
)

lives_remaining = 6
lives_text = c.create_text(
    canvas_width - 10,
    10,
    anchor="ne",
    font=game_font,
    fill="darkblue",
    text="Lives: " + str(lives_remaining),
)


eggs = []


def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = c.create_oval(
        x, y, x + egg_width, y + egg_height, fill=next(color_cycle), width=0
    )
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)


def move_eggs():
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        c.move(egg, 0, 30)
        if egg_y2 > canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)


def egg_dropped(egg):
    eggs.remove(egg)
    c.delete(egg)
    broken_sound.play()
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo(
            "Game Over",
            "Final Score: " + str(score) + " " + str(score2),
        )
        root.destroy()


def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    c.itemconfigure(lives_text, text="Lives: " + str(lives_remaining))


def check_catch():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 <= 40:
            eggs.remove(egg)
            c.delete(egg)
            catch_sound.play()
            increase_score(egg_score)
    root.after(100, check_catch2)


def check_catch2():
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher2)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 <= 40:
            eggs.remove(egg)
            c.delete(egg)
            catch_sound.play()
            increase_score2(egg_score)
    root.after(100, check_catch)


def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text, text="Score: " + str(score))


def increase_score2(points):
    global score2, egg_speed, egg_interval
    score2 += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    c.itemconfigure(score_text2, text="Score: " + str(score2))


def move_left(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x1 > 5:
        c.move(catcher, -20, 0)


def move_left2(event):
    (x1, y1, x2, y2) = c.coords(catcher2)
    if x1 > 5:
        c.move(catcher2, -20, 0)


def move_right(event):
    (x1, y1, x2, y2) = c.coords(catcher)
    if x2 < canvas_width - 5:
        c.move(catcher, 20, 0)


def move_right2(event):
    (x1, y1, x2, y2) = c.coords(catcher2)
    if x2 < canvas_width - 5:
        c.move(catcher2, 20, 0)


c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.bind("<a>", move_left2)
c.bind("<d>", move_right2)
c.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
rdnum = random.randint(1, 2)
if rdnum == 1:
    root.after(1000, check_catch)
    root.after(1000, check_catch2)
else:
    root.after(1000, check_catch2)
    root.after(1000, check_catch)
root.mainloop()
