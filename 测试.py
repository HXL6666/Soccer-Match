# -*- coding : utf-8 -*-
from tkinter import *
from tkinter import messagebox  # 弹窗库
import numpy as np


import tkinter as tk

# 定义数据
data = [
    [1, '球队A', 10, '5/3/2', '15/10', 5, 18],
    [2, '球队B', 10, '4/4/2', '12/8', 4, 16],
    [3, '球队C', 10, '4/2/4', '9/10', -1, 14],
    [4, '球队D', 10, '3/4/3', '7/7', 0, 13],
    [5, '球队E', 10, '3/4/3', '11/12', -1, 13],
    [6, '球队F', 10, '3/3/4', '8/10', -2, 12],
    [7, '球队G', 10, '3/3/4', '7/10', -3, 12],
    [8, '球队H', 10, '2/5/3', '9/11', -2, 11],
    [9, '球队I', 10, '2/5/3', '6/8', -2, 11],
    [10, '球队J', 10, '2/4/4', '7/8', -1, 10],
    [11, '球队K', 10, '2/4/4', '8/11', -3, 10],
    [12, '球队L', 10, '2/3/5', '9/13', -4, 9],
    [13, '球队M', 10, '2/3/5', '6/11', -5, 9],
    [14, '球队N', 10, '1/5/4', '7/9', -2, 8],
    [15, '球队O', 10, '1/4/5', '6/11', -5, 7],
    [16, '球队P', 10, '1/4/5', '7/12', -5, 7],
    [17, '球队Q', 10, '1/4/5', '7/13', -6, 7],
    [18, '球队R', 10, '0/5/5', '6/13', -7, 5]
]

# 创建窗口和Canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# 绘制表格标题
title = ['排名', '球队', '轮次', '胜/平/负', '进/失', '净胜球', '积分']
x0, y0 = 50, 50
for i, t in enumerate(title):
    canvas.create_text(x0 + i * 100, y0, text=t)

# 绘制表格内容
for i, row in enumerate(data):
    x0, y0 = 50, 80 + i * 30
    for j, cell in enumerate(row):
        if j == 0:
            # 排名列
            canvas.create_text(x0 + j * 100, y0, text=cell)
        else:
            # 其他列
            canvas.create_text(x0 + j * 100, y0, text=str(cell))

# 实时更新排名
def update_ranking():
    # 根据积分排序
    sorted_data = sorted(data, key=lambda x: x[-1], reverse=True)

    # 更新排名
    for i, row in enumerate(sorted_data):
        row[0] = i + 1

    # 清空Canvas
    canvas.delete('all')

    # 绘制表格标题
    title = ['排名', '球队', '轮次', '胜/平/负', '进/失', '净胜球', '积分']
    x0, y0 = 50, 50
    for i, t in enumerate(title):
        canvas.create_text(x0 + i * 100, y0, text=t)

    # 绘制表格内容
    for i, row in enumerate(sorted_data):
        x0, y0 = 50, 80 + i * 30
        for j, cell in enumerate(row):
            if j == 0:
                # 排名列
                canvas.create_text(x0 + j * 100, y0, text=cell)
            else:
                # 其他列
                canvas.create_text(x0 + j * 100, y0, text=str(cell))

    # 每隔一秒钟更新一次排名
    root.after(1000, update_ranking)

update_ranking()
root.mainloop()
