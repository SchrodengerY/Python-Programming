# Movie Chooser
# 演示复选框

from tkinter import *

class Application(Frame):
	""" GUI Application for favorite movie types. """
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		# 创建功能描述标签
		Label(self, text = "Choose your favorite movie types").grid(row = 0, column = 0, sticky = W)
		# 创建Comedy复选框
		self.likes_comedy = BooleanVar()
		Checkbutton(self,
					text = "Comedy",
					variable = self.likes_comedy,
					command = self.update_text).grid(row = 2, column = 0, sticky = W)
		# 创建drama复选框
		self.likes_drama = BooleanVar()
		Checkbutton(self,
					text = "Drama",
					variable = self.likes_drama,
					command = self.update_text).grid(row = 3, column = 0, sticky = W)
		# 创建romance复选框
		self.likes_romance = BooleanVar()
		Checkbutton(self,
					text = "Romance",
					variable = self.likes_romance,
					command = self.update_text).grid(row = 4, column = 0, sticky = W)
		# 创建用于显示的文本框
		self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
		self.results_txt.grid(row = 5, column = 0, columnspan = 3)

	def update_text(self):
		likes = ""

		if self.likes_comedy.get():
			likes += "You like comedic movies.\n"

		if self.likes_drama.get():
			likes += "You like dramatic movies.\n"

		if self.likes_romance.get():
			likes += "You like romantic movies."

		self.results_txt.delete(0.0, END)
		self.results_txt.insert(0.0, likes)

# 程序主体
root = Tk()
root.title("Movie Chooser")
app = Application(root)
root.mainloop()