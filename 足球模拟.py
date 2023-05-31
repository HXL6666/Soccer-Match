# -*- coding : utf-8 -*-
from random import *
from prettytable import PrettyTable


# 创建球队对象，包含队名，胜场等
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

    @property
    def points(self):  # 将积分作为一个属性，随着胜平场次实时变化
        return self.win * 3 + self.draw  # 赢加3分，平加1分，输不加分

    @property
    def round(self):  # 轮次
        return self.win + self.draw + self.loss

    @property
    def goal_difference(self):  # 净胜球
        return self.scored-self.conceded

    def show(self):  # 展示队伍实力
        print(self.__value)

    def wdl(self):  # 将"胜/平/负"封装在一起
        return "{}/{}/{}".format(self.win, self.draw, self.loss)

    def sc(self):   # 将"进/失"封装在一起
        return "{}/{}".format(self.scored, self.conceded)


teams = []
# teams_name = ["皇马", "巴萨", "拜仁", "曼城", "曼联", "切尔西", "利物浦", "阿森纳",
#               "热刺", "多特", "马竞", "巴黎", "西汉姆", "狼队", "布莱顿", "狼堡",
#               "摩纳哥", "马赛", "里昂", "尤文", "AC米兰", "国际米兰", "那不勒斯",
#               "罗马", "纽卡", "阿贾克斯", "埃弗顿", "本菲卡", "波尔图", "莱比锡"]
teams_stadium = [("皇马", "伯纳乌"), ("巴萨", "诺坎普"), ("拜仁", "安联"), ("曼城", "伊蒂哈德"),
                 ("曼联", "老特拉福德"), ("切尔西", "斯坦福桥"), ("利物浦", "安菲尔德"), ("阿森纳", "酋长"),
                 ("热刺", "新白鹿巷"), ("多特", "信号伊德纳公园"), ("马竞", "大都会"), ("巴黎", "王子公园"),
                 ("西汉姆", "伦敦奥林匹克体育场"), ("狼队", "莫利纽"), ("布莱顿", "阿米克斯"),
                 ("摩纳哥", "路易二世"), ("马赛", "韦洛德罗姆"), ("里昂", "里昂奥林匹克"), ("尤文", "阿连托·福尔图纳"),
                 ("AC米兰", "梅阿查"), ("国际米兰", "圣西罗"), ("那不勒斯", "圣保罗"), ("罗马", "奥林匹克"),
                 ("纽卡", "圣詹姆斯公园"), ("阿贾克斯", "约翰·克鲁伊夫"), ("埃弗顿", "古迪逊公园"),
                 ("本菲卡", "莱什波伦斯基"), ("波尔图", "多拉德"), ("莱比锡", "红牛竞技场"), ("狼堡", "大众竞技")]
number = 18
for name, field in teams_stadium[:number]:
    team = Team(name, field)
    teams.append(team)   # 一个包含球队实例的列表
print("新赛季开始，一共有{}支球队进行比赛".format(number))

table = PrettyTable()
table.field_names = ['排名', '球队', '轮次', '胜/平/负', '进/失', '净胜球', '积分']
table.align = 'c'
table.max_width["球队"] = 30
for i in range(number):
    table.add_row([i + 1, teams[i].name, teams[i].round, teams[i].wdl(), teams[i].sc(), teams[i].goal_difference, teams[i].points])

print(table.get_string())
