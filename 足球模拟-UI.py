# -*- coding : utf-8 -*-
 from 足球模拟 import *
from tkinter import *



class WinGUI(Tk):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=650, height=650, background='#f5eeee')
        self.canvas.pack()
        self.win()


    def win(self):
        for i in range(7):
            self.canvas.create_text(i*10+10,20,text=field_names[i])





class Win(WinGUI):
    def __init__(self):
        super().__init__()
        # self.__event_bind()


    # def __event_bind(self):
    #     self.canvas.bind("<Motion>", self.game_rules)




if __name__ == "__main__":
    win = Win()
    win.config(background="#D2B48C")
    win.mainloop()
