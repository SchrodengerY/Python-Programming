# Instructions

def instructions():
	"""Display game instructions."""
	print(
		"""
		Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
		This will be a showdown between your human brain and my silicon procesor.
		You will make your move known by entering a number, 0 - 8. The number
		will correspond to the board postion as illustracted:
						0 | 1 | 2
						---------
						3 | 4 | 5
						---------
						6 | 7 | 8
		Prepare yourself, human. The ultimate batin.\n
		"""
	)

# 主程序
print("Here are the instructions to the Tic-Tac-Toe game:")
instructions()
print("Here they are again:")
instructions()
print("You probably understand the game by now.")

# Receive and Return

def display(message):
	print(message)

def give_me_five():
	five = 5
	return five

def ask_yes_no(question):
	"""Ask a yes or no question."""
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response

# 程序主体
display("Here's a message for you.\n")

number = give_me_five()
print("Here's what I got from give_me_five():", number)

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

# Global Reach

def read_global():
	print("From inside the local scope of read_global(), value is:", value)

def shadow_global():
	value = -10
	print("From inside the local scope of shadow_global(), value is:", value)

def change_global():
	global value
	value = -10
	print("From inside the local scope of change_global(), value is:", value)

# 程序主题
value = 10
print("In the global scope, value has been set to:", value, "\n")

read_global()
print("Back in the global scope, value is still:", value, "\n")

change_global()
print("Back in the global scope, value has now changed to:", value)



