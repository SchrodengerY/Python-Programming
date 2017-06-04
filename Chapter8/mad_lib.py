# Mad Lib
# 根据用户的输入创建一个故事

from tkinter import *

class Application(Frame):
	""" GUI application that creates a story based on user input. """
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		""" Create widgets to get story information and to display story. """
		# 创建说明标签
		Label(self,
			  text = "Enter information for a new story").grid(row = 0, column = 0, sticky = W)

		# 创建用于人名的标签和文本框
		Label(self,
			  text = "Person: ").grid(row = 1, column = 0, sticky = W)
		self.person_ent = Entry(self)
		self.person_ent.grid(row = 1, column = 1, sticky = W)

		# 创建用于复数名词的标签和文本框
		Label(self,
			  text = "Plural Noun:").grid(row = 2, column = 0, sticky = W)
		self.noun_ent = Entry(self)
		self.noun_ent.grid(row = 2, column = 1, sticky = W)

		# 创建用于动词的标签和文本框
		Label(self,
			  text = "Verb:").grid(row = 3, column = 0, sticky = W)
		self.verb_ent = Entry(self)
		self.verb_ent.grid(row = 3, column = 1, sticky = W)

		# 创建用于形容词复选框和标签
		Label(self,
			  text = "Adjective(s):").grid(row = 4, column = 0, sticky = W)

		# 创建itchy复选框
		self.is_itchy = BooleanVar()
		Checkbutton(self,
					text = "itchy",
					variable = self.is_itchy).grid(row = 4, column = 1, sticky = W)

		# 创建joyous复选框
		self.is_joyous = BooleanVar()
		Checkbutton(self,
					text = "joyous",
					variable = self.is_joyous).grid(row = 4, column = 2, sticky = W)

		# 创建electric复选框
		self.is_electric = BooleanVar()
		Checkbutton(self,
					text = "electric",
					variable = self.is_electric).grid(row = 4, column = 3, sticky = W)

		# 创建用于身体部位单选框的标签
		Label(self,
			  text = "Body Part:").grid(row = 5, column = 0, sticky = W)

		# 创建表示单个身体部位的变量
		self.body_part = StringVar()
		self.body_part.set(None)

		# 创建身体部位复选框
		body_parts = ["bellybutton", "big toe", "medulla oblongata"]
		column = 1
		for part in body_parts:
			Radiobutton(self,
						text = part,
						variable = self.body_part,
						value = part).grid(row = 5, column = column, sticky = W)
			column += 1

		# 创建提交按钮
		Button(self,
			   text = "Click for story",
			   command = self.tell_story).grid(row = 6, column = 0, sticky = W)
		self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
		self.story_txt.grid(row = 7, column = 0, columnspan = 4)

	def tell_story(self):
		""" Fill text box with new story based on user input. """
		# 从GUI获取值
		person = self.person_ent.get()
		noun = self.noun_ent.get()
		verb = self.verb_ent.get()
		adjectives = ""
		if self.is_itchy.get():
			adjectives += "itchy, "
		if self.is_joyous.get():
			adjectives += "joyous, "
		if self.is_electric.get():
			adjectives += "electric, "
		body_part = self.body_part.get()

		# 创建故事
		story = "The famous explorer "
		story += person
		story += " had nearly given up a life-long quest to find The Lost City of "
		story += noun.title()
		story += " when on day, the "
		story += noun
		story += " found "
		story += person + ". "
		story += "A strong, "
		story += adjectives
		story += "peculiar feeling overwhelmed the explorer. "
		story += "After all this time, the quest was finally over. A tear came to "
		story += person + "'s "
		story += body_part + ". "
		story += "And then, the "
		story += noun
		story += " promptly devoured "
		story += person + ". "
		story += "The moral of the story? Be careful what you "
		story += verb
		story += " for."

		# 显示故事
		self.story_txt.delete(0.0, END)
		self.story_txt.insert(0.0, story)

# 程序主体
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()