# Word Jumble
#
# 计算机随机挑选一个单词，然后把它弄乱
# 玩家必须猜出本来的单词

import random

WORDS = ("python","jumble","easy","difficult","answer","xylophone")
word = random.choice(WORDS)
correct = word

jumble = ""

while word:
	position = random.randrange(len(word))
	jumble += word[position]
	word = word[:position] + word[(position+1):]

# 开始游戏
print(
	"""
		Welcome to Word Jumble!

	Unscramble the letters to make a word.
 (Press the enter key at the prompt to quit.)
	"""
)
print("The jumble is:",jumble)

# 获取玩家答案
guess = input("\nYour answer: ")
while guess != correct and guess != '':
	print("Sorry, that's not it.")
	guess = input("Your guess: ")
if guess == correct:
	print("That's it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")