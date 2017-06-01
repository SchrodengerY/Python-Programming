# 电视机频道和音量

class Television(object):
	def __init__(self,channel = 1, vol = 1):
		self.channel = int(channel)
		self.vol = int(vol)

	def channel_vision(self):
		if self.channel == 1:
			print("CCTV 1 - 新闻联播")
		elif self.channel == 2:
			print("CCTV 2 - 经济与法")
		elif self.channel == 3:
			print("CCTV 3 - 同一首歌")
		elif self.channel == 4:
			print("CCTV 4 - 海峡两岸")
		elif self.channel == 5:
			print("CCTV 5 - 体育频道")
		else:
			print("-----无信号-----")

	def channel_change(self,channel):
		if channel == "+":
			self.channel += 1
			if self.channel > 5:
				self.channel = self.channel % 5
		elif channel == "-":
			self.channel -= 1
			if self.channel < 1:
				self.channel = 5
		else:
			self.channel = int(channel)

	def vol_change(self,vol):
		if vol == "+":
			self.vol += 10
		else:
			self.vol -= 10
		if self.vol >= 50:
			print("It's too loud!!!")
		print("The current vol is:",self.vol)

def main():
	print(
		"""
		\t\t\t\t _________________________________________
		\t\t\t\t|                                         |
		\t\t\t\t|                                         |
		\t\t\t\t|                                         |
		\t\t\t\t|                                         |
		\t\t\t\t|         This is a big television.       |
		\t\t\t\t|                                         |
		\t\t\t\t|          You can use number(1-5)        |
		\t\t\t\t|      "+" or "-" to change the channel   |
		\t\t\t\t|                                         |
		\t\t\t\t|          Meanwhile, you can use         |
		\t\t\t\t|        "+" or "-" to change the vol     |
		\t\t\t\t|                                         |
		\t\t\t\t|       The red button is to close TV     |
		\t\t\t\t|                                         |
		\t\t\t\t|                                         |
		\t\t\t\t|_________________________________________|""")

	tel = Television()
	red_button = 0
	while(not red_button):
		channel = input("\nChange the channel:")
		tel.channel_change(channel)
		tel.channel_vision()
		vol = input("\nChange the vol:")
		tel.vol_change(vol)
		rest = input("If you want to take a rest(y/n):")
		if rest.lower() == "y":
			red_button = 1
		else:
			red_button = 0

main()