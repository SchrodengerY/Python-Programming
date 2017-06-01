# Simple Critter
# 演示一个简单的类和对象

class Critter(object):
	"""A virtual pet"""
	def talk(self):
		print("Hi. I'm an instance of calss Critter.\n\n")

# 程序主体
crit = Critter()
crit.talk()

# Constructor Critter
# 演示构造器

class Critter(object):
	"""A virtual pet"""
	def __init__(self):
		print("A new critter has been born!")

	def talk(self):
		print("\nHi. I'm an instance of class Critter.")

# 程序主体
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

# Attribute Critter
# 演示创建和访问对象的特性

class Critter(object):
	"""A virtual pet"""
	def __init__(self,name):
		print("A new critter has been born!")
		self.name = name

	def __str__(self):
		rep = "Critter object\n"
		rep += "name: " + self.name + "\n"
		return rep

	def talk(self):
		print("Hi. I'm", self.name, "\n")

# 程序主体
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randolph")
crit2.talk()

print("Printing crit1:")
print(crit1)

# Classy Critter
# 演示类特性和静态方法

class Critter(object):
	"""A virtual pet"""
	total = 0

	@staticmethod
	def status():
		print("\nThe total number of critters is", Critter.total)

	def __init__(self,name):
		print("A critter has been born!")
		self.name = name
		Critter.total += 1

# 程序主体
print("Accessing the class attribute critter.total:", end=" ")
print(Critter.total)
print("\nCreating critters.")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status()

print("\nAccessing the class attribute through an object:", end=" ")
print(crit1.total)

# Private Critter
# 演示私有变量和方法

class Critter(object):
	"""A virtual pet"""
	def __init__(self,name,mood):
		print("A new critter has been born!")
		self.name = name         # 公有特性
		self.__mood = mood       # 私有特性
	def talk(self):
		print("\nI'm", self.name)
		print("Right now I feel", self.__mood,"\n")

	def __private_method(self):
		print("This is a private method.")

	def public_method(self):
		print("This is a public method.")
		self.__private_method()

# 程序主体
crit = Critter(name = "Poochie", mood = "happy")
crit.talk()
crit.public_method()

# Property Critter
# 演示属性

class Critter(object):
	"""A virtual pet"""
	def __init__(self,name):
		print("A new critter has been born")
		self.__name = name

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, new_name):
		if new_name == "":
			print("A critter's name can't be the empty string.")
		else:
			self.__name = new_name
			print("Name changes successful.")

	def talk(self):
		print("\nHi, I'm", self.name)

# 程序主体
crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critter's name to Randolph...")
crit.name = "Randolph"
print("My critter's name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critter's name to the empty string...")
crit.name = ""
print("My critter's name is:", end=" ")
print(crit.name)

#注意，程序中调用的是.name而不是.__name。name是property而__name是private 变量


