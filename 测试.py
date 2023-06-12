# -*- coding : utf-8 -*-
from tkinter import *
from tkinter import messagebox  # 弹窗库
import numpy as np

from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()

x1, y1 = 50, 50
x2, y2 = 150, 150
side_length = x2 - x1

# 绘制正方形
canvas.create_rectangle(x1, y1, x2, y2)

# 设置虚线样式
canvas.itemconfig(1, dash=(side_length/3, side_length/3))

root.mainloop()
