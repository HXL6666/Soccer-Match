# -*- coding : utf-8 -*-
from 足球赛程模拟器.足球模拟 import *
from tkinter import *
from random import *


class WinGUI(Tk):

    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self, width=650, height=770, background='#f5eeee')
        self.canvas.pack(side=LEFT)
        self.win()
        self.table()

    # 使程序居中
    def win(self):
        self.title("足球赛程模拟器")
        width = 900
        height = 770
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)  # 窗口大小不可调节

    # 创建排行榜框架,并初始化
    def table(self):
        self.canvas.create_rectangle(20, 5, 430, 35, fill='#c0e1ff', outline='#c0e1ff')  # 排头背景，矩形框
        self.canvas.create_text(50, 20, text='排名')  # 排头
        self.canvas.create_text(110, 20, text='球队')
        self.canvas.create_text(200, 20, text='轮次')
        self.canvas.create_text(250, 20, text='胜/平/负')
        self.canvas.create_text(300, 20, text='进/失')
        self.canvas.create_text(350, 20, text='净胜球')
        self.canvas.create_text(400, 20, text='积分')
        for i in range(number):  # 初始化表格
            self.canvas.create_line(20, i * 40 + 75, 430, i * 40 + 75, width=0.1, fill="#c4c2c2")
            self.canvas.create_text(50, 55 + i * 40, text=i + 1)  # 初始第一列排序数字
            self.canvas.create_text(110, 55 + i * 40, text=teams[i].name)
            self.canvas.create_text(200, 55 + i * 40, text=teams[i].round)
            self.canvas.create_text(250, 55 + i * 40, text=teams[i].wdl())
            self.canvas.create_text(300, 55 + i * 40, text=teams[i].sc())
            self.canvas.create_text(350, 55 + i * 40, text=teams[i].goal_difference)
            self.canvas.create_text(400, 55 + i * 40, text=teams[i].points)


# 创建球队类，包含队名，胜场等
class Team:
    def __init__(self, name, home, win=0, loss=0, draw=0, scored=0, conceded=0):
        self.name = name  # 球队名
        self.home_field = home  # 主场
        self.win = win  # 胜场
        self.loss = loss  # 负场
        self.draw = draw  # 平局
        self.scored = scored  # 进球
        self.conceded = conceded  # 失球
        self.__value = randint(1, 10)  # 实力

    @property  # 将积分作为一个属性，随着胜平场次实时变化
    def points(self):
        return self.win * 3 + self.draw  # 赢加3分，平加1分，输不加分

    @property  # 轮次
    def round(self):
        return self.win + self.draw + self.loss

    @property  # 净胜球
    def goal_difference(self):
        return self.scored - self.conceded

    # 展示队伍实力
    def show(self):
        print(self.__value)

    # 将"胜/平/负"封装在一起
    def wdl(self):
        return "{}/{}/{}".format(self.win, self.draw, self.loss)

    # 将"进/失"封装在一起
    def sc(self):
        return "{}/{}".format(self.scored, self.conceded)


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        # self.__event_bind()

    # def __event_bind(self):
    #     self.canvas.bind("<Motion>", self.game_rules)


# 将球队和主场写进实例中
for name, field in teams_stadium[:number]:
    team = Team(name, field)
    teams.append(team)  # 一个包含球队实例的列表
# print("新赛季开始，一共有{}支球队进行比赛".format(number))

if __name__ == "__main__":
    win = Win()
    win.config(background="#D2B48C")
    win.mainloop()
