# for循环
# Loopy String

word = input("Enter a word: ")
print("Here's each letter in your word:")
for letter in word:
	print(letter)

# Counter

print("Counting:")
for i in range(10):
	print(i, end=' ')

print("\n\nCounting by fives:")
for i in range(0, 50, 5):
	print(i, end=' ')

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
	print(i, end=' ')

# Random Access
import random

word = "INdex"
print("The word is:",word,"\n")

high = len(word)
low = -len(word)

for i in range(10):
	position = random.randrange(low, high)
	print("word[",position,"]\t", word[position])

# 使用全大写创建的是常量，一般不作修改。

# 使用元组
# Hero's Inventory

# 创建一个新的元组
inventory = ()

if not inventory:
	print("You are empty-handed.")

input("\nPress the enter key to continue.")

inventory = ("sword","armor","shield","healing potion")

print("\nThe tuple inventory is:")
print(inventory)

print("\nYour items:")
for item in inventory:
	print(item)

