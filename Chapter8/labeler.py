# Labeler
# 演示标签

from tkinter import *

# 创建根窗体
root = Tk()
root.title("Labeler")
root.geometry("200x50")    # 中间的是lower case "x"

# 在根窗体中创建一个框架，用它来承载其他的小部件
app = Frame(root)
app.grid()

# 在框架中创建一个标签
lbl = Label(app, text = "I'm a label.")
lbl.grid()

# 启动根窗体的事件循环
root.mainloop()