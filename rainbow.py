import tkinter as tk
import random as r


class CustomButton:
    def __init__(self, master, text="", width=1000, height=500):
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.pack()

        self.bg_color = "red"
        self.fg_color = r.choice(color_list)

        # 创建矩形（按钮背景）和文字
        self.rect = self.canvas.create_rectangle(
            2, 2, width - 2, height - 2, fill=self.bg_color
        )
        self.text = self.canvas.create_text(
            width / 2, height / 2, text=text, fill=self.fg_color
        )

        # 绑定点击事件
        self.canvas.bind("<Button-1>", self.click)

    def click(self, event):
        self.bg_color = r.choice(color_list)
        self.fg_color = r.choice(color_list)
        self.canvas.itemconfig(self.rect, fill=self.bg_color)
        self.canvas.itemconfig(self.text, fill=self.fg_color)


def make_button(w, text):
    button = CustomButton(w, text)


color_list = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "gray",
    "black",
    "white",
]
# w = tk.Tk()
# w.title("My Window")
# w.geometry("1300x1000")

# button = CustomButton(w)

# w.mainloop()
