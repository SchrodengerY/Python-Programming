# Lazy Buttons
# 演示创建按钮

from tkinter import *

# 创建根窗体
root = Tk()
root.title("Lazy Buttons")
root.geometry("200x85")

# 在窗体中创建一个框架，用来承载其他小部件
app = Frame(root)
app.grid()

# 在框架中创建一个按钮
bttn1 = Button(app, text = "I do nothing!")
bttn1.grid()

# 创建app框架中的第二个按钮
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Me too!")

# 创建app框架中的第三个按钮
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "Same here!"

# 启动根窗体的事件循环
root.mainloop()