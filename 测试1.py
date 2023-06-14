from tkinter import *
from tkinter import messagebox  # 弹窗库
import numpy as np


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.width = 900
        self.height = 650
        self.canvas = Canvas(self, width=self.width, height=self.height, background='#D2B48C')
        self.canvas.pack()
        self.count_num = self.__count_num()


    def __count_num(self):
        self.canvas.create_oval(700, 125, 720, 145, fill='black')
        num_black = self.canvas.create_text(740, 135, text=0)
        self.canvas.create_oval(800, 125, 820, 145, fill='white')
        num_white = self.canvas.create_text(840, 135, text=0)
        return num_black, num_white

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        self.canvas.bind("<Button -1>", self.load)

    def load(self, event):
        self.canvas.delete(ALL)
        self.canvas.after(100, self.canvas.delete, self.predict)

if __name__ == "__main__":
    win = Win()
    win.mainloop()
