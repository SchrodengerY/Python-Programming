# 猜单词游戏
# 大小写均可
import random

WORDS = ("Kobe","Paul","Curry","James","Jordan","YaoMing")
word = random.choice(WORDS)
tries = 1
temp = 0

while(tries <= 5):
	flag = 0
	print("The length of the word is:",len(word),"\n")
	letter = input("You can ask the computer if the letter is in word:")
	for let in word:
		if let.lower() == letter.lower():
			flag = 1
			print("Yes.\n")
			break
	if not flag:
		print("No.\n")
	word_guess = input("The word you guess is:")
	if word_guess.lower() == word.lower():
		temp = 1
		print("Genius!")
		break
	tries += 1
if not temp:
	print("Sorry, you failed. The word is:",word,"\n")