# Lazy Buttons 2
# 演示如何通过类来使用Tkinter

from tkinter import *

class Application(Frame):
	"""A GUI application with three buttons."""
	def __init__(self, master):
		"""Initialize the Frame."""
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create three buttons that do nothing. """
		# 创建第一个按钮
		self.bttn1 = Button(self, text = "I do nothing.")
		self.bttn1.grid()

		# 创建第二个按钮
		self.bttn2 = Button(self)
		self.bttn2.grid()
		self.bttn2.configure(text = "Me too!")

		# 创建第三个按钮
		self.bttn3 = Button(self)
		self.bttn3.grid()
		self.bttn3["text"] = "Same here!"

# 程序主体
root = Tk()
root.title("Lazy Buttons 2")
root.geometry("200x85")

app = Application(root)

root.mainloop()