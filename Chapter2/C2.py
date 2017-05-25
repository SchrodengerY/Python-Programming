# Guess my number
#
# 计算机从1-100之间随机挑选一个数字
# 玩家尝试把它猜出来，计算机要让他知道猜高了还是猜低了
# 或者猜对了

import random

print("\tWelcome to 'Guess My Nuber'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# 设置初始值
the_number = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

# 猜测循环
while guess != the_number:
	tries += 1
	if guess > the_number:
		print("Lower...")
	else:
		print("Higher...")
	guess = int(input("Take a guess: "))

# 表示祝贺
print("You guessed it! The number is", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress any key to exit.")
