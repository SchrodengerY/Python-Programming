# Critter Caretaker
# 一只需要细心呵护的虚拟宠物
# 增加了一个后门程序，可以查看对象个特性确切值
# 在choice输入99可以查看属性

class Critter(object):
	"""A virtual pet"""
	def __init__(self, name, hunger = 0, boredom = 0):
		self.name = name
		self.hunger = hunger
		self.boredom = boredom

	def __str__(self):
		rep = "Name:" + self.name + " " + "Hunger:" + str(self.hunger) + " " + "Boredom:" + str(self.boredom) + "\n"
		return rep

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "HappY"
		elif 5 <= unhappiness <= 10:
			m = "oK"
		elif 11 <= unhappiness <= 15:
			m = "frUstrAted"
		else:
			m = "mAD"
		return m

	def talk(self):
		print("I'm", self.name, "and I feel", self.mood, "now.\n")
		#print("Food:",self.hunger,"Fun:",self.boredom)
		self.__pass_time()

	def eat(self, food = 4):
		print("Brruppp. Thank you.")
		self.hunger -= int(food)
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()

	def play(self, fun = 4):
		print("Wheee!")
		self.boredom -= int(fun)
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()

def main():
	crit_name = input("What do you want to name your critter?: ")
	crit = Critter(crit_name)

	choice = None
	while choice != "0":
		print(
			"""
			Critter Caretaker

			0 - Quit
			1 - Listen to your critter
			2 - Feed your critter
			3 - Play with your critter
			"""
		)

		choice = input("Choice: ")
		print()

		# 退出
		if choice == "0":
			print("Good-Bye.")
		elif choice == "1":
			crit.talk()
		elif choice == "2":
			crit.eat()
		elif choice == "3":
			crit.play()
		elif choice == "99":
			print(crit)
		else:
			print("\nSorry, but",choice,"isn't a valid choice.")

main()
print("\n\nPress the enter key to exit.")