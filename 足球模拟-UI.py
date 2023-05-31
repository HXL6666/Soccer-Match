# -*- coding : utf-8 -*-
# from 足球模拟 import *
from tkinter import *


class WinGUI(Tk):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=650, height=650, background='#f5eeee')
        self.canvas.pack()
        self.line()

    def line(self):
        for i in range(15):
            ww = 1
            if (i == 0) or (i == 14):  # 边界加粗
                ww = 2
            self.canvas.create_line(45, i * 40 + 45, 605, i * 40 + 45, width=ww)  # 15条横线
            self.canvas.create_text(30, i * 40 + 45, text=i + 1)  # 横坐标
            self.canvas.create_line(i * 40 + 45, 45, i * 40 + 45, 605, width=ww)  # 15条竖线
            self.canvas.create_text(i * 40 + 45, 30, text=i + 1)  # 纵坐标


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()


    def __event_bind(self):
        self.canvas.bind("<Motion>", self.game_rules)

    def game_rules(self, event):
        for i in range(45, 645, 40):
            for j in range(45, 645, 40):
                l1 = i - 15
                l2 = i + 15
                r1 = j - 15
                r2 = j + 15
                if l1 <= event.x <= l2 and r1 <= event.y <= r2:
                    self.canvas.create_rectangle(i - 15, j - 15, i + 15, j + 15, dash=(1, 1), outline="blue")
                    self.canvas.pack()


if __name__ == "__main__":
    win = Win()
    win.config(background="#D2B48C")
    win.mainloop()
