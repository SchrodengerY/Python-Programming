# Longevity
# 演示Text和Entry小部件，以及Grid布局管理器

from tkinter import *

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		# 创建用于说明的标签
		self.inst_lbl = Label(self, text = "Enter password for the secret of"
										   "longevity")
		# 用Grid布局管理器指定标签的具体位置
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		# row为行号，column为列号，columnspan表示占用的列数，rowspan表示占用的行数，sticky用于调整对齐方式
		self.pw_lbl = Label(self, text = "Password: ")
		self.pw_lbl.grid(row = 1, column = 0, sticky = W)

		# 创建用于接受密码的Entry小部件
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row = 1, column = 1, sticky = W)

		# 创建一个提交按钮
		self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
		self.submit_bttn.grid(row = 2, column = 0, sticky = W)

		# 创建用于显示消息的Text小部件
		self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
		self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)

	def reveal(self):
		"""Display message based on password. """
		contents = self.pw_ent.get()
		if contents == "secret":
			message = "Here's the secret to living to 100: live to 99" \
					  "and the be VERY careful."
		else:
			message = "That's not the correct password, so I can't share" \
					  "the secret with you."
		self.secret_txt.delete(0.0, END)
		# 0.0表示第0行，第0列（即绝对起始位）
		self.secret_txt.insert(0.0, message)

# 程序主体
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)
root.mainloop()