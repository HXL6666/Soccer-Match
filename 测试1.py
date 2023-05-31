# -*- coding : utf-8 -*-
from tkinter import *
class WinGUI(Tk):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=650, height=650, background='#f5eeee')
        self.canvas.pack()
        self.line_width = 1
        self.line_length = 40
        self.draw_board()

    def draw_board(self):
        for i in range(15):
            if i == 0 or i == 14:
                self.line_width = 2
            else:
                self.line_width = 1
            x = i * self.line_length + 45
            self.canvas.create_line(x, 45, x, 605, width=self.line_width)
            self.canvas.create_text(x, 30, text=i + 1)
            self.canvas.create_line(45, x, 605, x, width=self.line_width)
            self.canvas.create_text(30, x, text=i + 1)

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        self.canvas.bind("<Motion>", self.game_rules)

    def game_rules(self, event):
        for i, x in enumerate(range(45, 645, 40)):
            for j, y in enumerate(range(45, 645, 40)):
                if x - self.line_length <= event.x <= x + self.line_length and \
                   y - self.line_length <= event.y <= y + self.line_length:
                    cx, cy = x, y
                    self.canvas.create_oval(cx - 15, cy - 15, cx + 15, cy + 15, dash=(1, 1), outline="blue")

if __name__ == "__main__":
    win = Win()
    win.config(background="#D2B48C")
    win.mainloop()
