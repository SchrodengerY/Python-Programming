# 摘自百度
# 利用IDE产生窗体程序
# 注意tk.mainloop()语句

from tkinter import *

tk = Tk()
# 修整窗体
tk.title("Simple GUI")
# tk.geometry("200*100")

canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
tk.mainloop()      # 进入窗体的事件循环

def movetriangel(event):
	canvas.move(1,5,0)

canvas.bind_all('<KeyPress-Return>', movetriangel)

