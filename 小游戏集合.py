# -*- coding : utf-8 -*-
import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title("My GUI")

# 设置窗口大小
window.geometry("500x300")

# 允许调整大小
window.resizable(True, True)

# 添加标签
label = tk.Label(text="Hello, World!")
label.pack()

# 运行窗口
window.mainloop()
