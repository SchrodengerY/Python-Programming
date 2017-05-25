# Guess My Number - Version 2.0
# This is a game for computer

import random

num = int(input("Please input a number between 1-100 for computer to guess:"))
tries = 1
min = 1
max = 100
guess = random.randint(min,max)

while(num != guess):
	print("The guess number for computer is:",guess)
	if(num > guess):
		print("Lower...")
		min = guess+1
		guess = random.randint(min,max)
	else:
		print("Higher...")
		max = guess-1
		guess = random.randint(min,max)
	tries += 1

print("Great! The true number is:", num)
print("The tries is:",tries)



