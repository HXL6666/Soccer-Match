from tkinter import *
class GameBoard(Tk):
    def __init__(self):
        super().__init__()
        self.win()
        self.canvas = Canvas(self, width=650, height=650, background='#D2BE96')  # #f5eeee
        self.canvas.pack(side=LEFT)
        self.canvas.create_rectangle(100, 100, 200, 200, outline='red', width=3)

    def win(self):            # 使窗口居中
        self.title("双人五子棋")
        width = 900
        height = 650
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)     # 窗口大小不可调节

if __name__ == "__main__":
    win1 = GameBoard()
    win1.mainloop()