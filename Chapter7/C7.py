# 面向对象的编程 II
# 多个类

# Alien Blaster
# 演示对象之间的交互

class Player(object):
	"""A Player in a shooter game."""
	def blast(self, enemy):
		print("The player blasts an enemy.\n")
		enemy.die()

class Alien(object):
	"""An alien in a shooter game."""
	def die(self):
		print("The alien gasps and says, 'Oh, this is it. This is the big one.'\n")

# 程序主体
print("\t\tDeath of an Alien\n")

hero = Player()
invader = Alien()
hero.blast(invader)


# Playing Cards
# 演示对象组合

class Card(object):
	"""A playing card."""
	RANKS = ["A", "2", "3", "4", "5", "6", "7",
			 "8", "9", "10", "J", "Q", "K"]          # 表示牌面大小
	SUITS = ["c", "d", "h", "s"]                     # 表示花色

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		rep = self.rank + self.suit
		return rep

class Hand(object):
	"""A hand of playing cards."""
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "<empty>"
		return rep

	def clear(self):
		self.cards = []

	def add(self, card):
		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)

# 程序主体
card1 = Card(rank = "A", suit = "c")
print("Printing a Card object:")
print(card1)

card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
print("\nPrinting the rest of the objects individually:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nPrinting my hand before I add any cards:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nPrinting my hand after adding 5 cards:")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nGave the first two cards from my hand to your hand.")
print("Your hand:")
print(your_hand)
print("My hand:")
print(my_hand)

my_hand.clear()
print("\nMy hand after clearing it:")
print(my_hand)


# Playing Cards 2.0
# 演示继承-类扩展

class Card(object):
	"""A playing card."""
	RANKS = ["A", "2", "3", "4", "5", "6", "7",
			 "8", "9", "10", "J", "Q", "K"]          # 表示牌面大小
	SUITS = ["c", "d", "h", "s"]                     # 表示花色

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		rep = self.rank + self.suit
		return rep

class Hand(object):
	"""A hand of playing cards."""
	def __init__(self):
		self.cards = []

	def __str__(self):
		if self.cards:
			rep = ""
			for card in self.cards:
				rep += str(card) + " "
		else:
			rep = "<empty>"
		return rep

	def clear(self):
		self.cards = []

	def add(self, card):
		self.cards.append(card)

	def give(self, card, other_hand):
		self.cards.remove(card)
		other_hand.add(card)
class Deck(Hand):                # derived class
	"""A deck of playing cards. """
	def populate(self):
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				self.add(Card(rank, suit))

	def shuffle(self):
		import random
		random.shuffle(self.cards)

	def deal(self, hands, per_hand = 1):
		for rounds in range(per_hand):
			for hand in hands:
				if self.cards:
					top_card = self.cards[0]
					self.give(top_card, hand)
				else:
					print("Can't continue deal. Out of cards!")

# 程序主体
deck1 = Deck()
deck1.populate()

print("\nPopulated the deck.")
print("Deck:")
print(deck1)

deck1.shuffle()
print("\nShuffled the deck.")
print("Deck:")
print(deck1)

my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]

deck1.deal(hands, per_hand = 5)
print("\nDealt 5 cards to my hand and your hand.")
print("My hand:")
print(my_hand)
print("Your hand:")
print(your_hand)
print("Deck:")
print(deck1)

deck1.clear()
print("\nCleared the deck.")


# Playing Cards 3.0
# 演示继承--重写方法

class Card(object):
	"""A playing card."""
	RANKS = ["A", "2", "3", "4", "5", "6", "7",
			 "8", "9", "10", "J", "Q", "K"]          # 表示牌面大小
	SUITS = ["c", "d", "h", "s"]                     # 表示花色

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	def __str__(self):
		rep = self.rank + self.suit
		return rep

class Unprintable_Card(Card):
	"""A Card that won't reveal its rank or suit when printed. """
	def __str__(self):
		return "<unprintable>"

class Positionable_Card(Card):
	"""A Card that can be face up or face down."""
	def __init__(self, rank, suit, face_up = True):
		super(Positionable_Card, self).__init__(rank, suit)
		self.is_face_up = face_up

	def __str__(self):
		if self.is_face_up:
			rep = super(Positionable_Card, self).__str__()
		else:
			rep = "XX"
		return rep

	def flip(self):
		self.is_face_up = not self.is_face_up

# 程序主体
card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Printing a Card object:")
print(card1)

print("\nPrinting an Unprintable_Card object:")
print(card2)

print("\nPrinting a Positionable_Card object:")
print(card3)

print("Flipping the Positionable_Card object.")
card3.flip()

print("Printing the Positionable_Card object:")
print(card3)


