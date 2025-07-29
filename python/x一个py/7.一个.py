import tkinter as tk
import random


def click():
    if msg:
        b.configure(text=msg.pop(random.randint(0, len(msg) - 1)))
    else:
        b.configure(text="点名结束")


root = tk.Tk()
root.title("点名")
root.geometry("800x600")
msg = input().split()
b = tk.Button(root, text="点名", command=click)
b.place(x=100, y=100)
root.mainloop()
