from tkinter import *

class Win(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=650, height=650, background='#D2BE96')  # #f5eeee
        self.canvas.pack(side=LEFT)
        self.__event_bind()
        self.predict = None
        self.x = None

    # 事件绑定
    def __event_bind(self):
        self.canvas.bind("<Motion>", self.game_rules)

    def game_rules(self, event):
        # j = (event.x - 45) / 40
        # i = (event.y - 45) / 40  # 上临近i行，左临近j列，从左到右，从上到下
        # if (event.x - 45) % 40 > 20:
        #     j += 1
        # if (event.y - 45) % 40 > 20:
        #     i += 1
        # self.predict = self.canvas.create_rectangle(i - 15, j - 15, i + 15, j + 15, dash=(3, 1),
        #                                             outline="blue")

        self.x = self.canvas.create_text(300, 300, text='x,y:{},{}'.format(event.x, event.y))
        self.canvas.delete(self.x)
        # self.canvas.after(2000, self.canvas.delete, self.x)

        # if self.predict:  # 不断删除，不断更新
        #     self.canvas.delete(self.predict)

if __name__ == "__main__":
    win = Win()
    win.config(background="#D2B48C")
    win.mainloop()