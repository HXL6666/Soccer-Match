from tkinter import *
from tkinter import messagebox  # 弹窗库
import numpy as np


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=650, height=650, background='#D2BE96')  # #f5eeee
        self.canvas.pack(side=LEFT)
        self.game_line()
        self.__event_bind()
        self.predict = None


    def __event_bind(self):
        self.canvas.bind("<Motion>", self.game_rules)

    def game_line(self):
        for i in range(15):
            ww = 1
            if (i == 0) or (i == 14):  # 边界加粗
                ww = 2
            self.canvas.create_line(45, i * 40 + 45, 605, i * 40 + 45, width=ww)  # 15条横线
            self.canvas.create_text(30, i * 40 + 45, text=i + 1)  # 横坐标
            self.canvas.create_line(i * 40 + 45, 45, i * 40 + 45, 605, width=ww)  # 15条竖线
            self.canvas.create_text(i * 40 + 45, 30, text=i + 1)  # 纵坐标


    def game_rules(self, event):
        if 45 <= event.x <= 605 and 45 <= event.y <= 605:
            i = (event.x - 45) // 40
            j = (event.y - 45) // 40  # 上临近j行，左临近i列，从左到右，从上到下
            if (event.x - 45) % 40 > 20:
                i += 1
            if (event.y - 45) % 40 > 20:
                j += 1
            self.predict = self.canvas.create_rectangle(i*40 + 30, j*40 + 30, i*40 + 60, j*40 + 60, dash=(1), outline="blue")
            if self.predict:  # 不断删除，不断更新
                self.canvas.after(70, self.canvas.delete, self.predict)

if __name__ == "__main__":
    win = WinGUI()
    win.config(background="#D2B48C")
    win.mainloop()