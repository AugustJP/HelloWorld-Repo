import random


class Die:
	def __init__(self, numSides):
		self.numSides = numSides
		self.value = 1

	def roll(self):
		self.value = random.randint(1, self.numSides)
	
	def getValue(self):
		return self.value
	
	def __str__(self):
		return(f"You rolled a {self.value}")
	
	def __add__(self, val2):
		return self.value + val2.value
		
	def __gt__(self, val2):
		return self.value > val2.value
		


class Player:
	def __init__(self, name):
		self.name = name
		self.die1 = Die(6)
		self.die2 = Die(10)
		
	def rollDice(self):
		self.die1.roll()
		self.die2.roll()
		
	def getDiceValue(self):
		return self.die1 + self.die2
	def __str__(self):
		return(f"{self.name} {self.getDiceValue()}")
		
class HighTwoGame:
	def __init__(self, player1, player2):
		self.player1 = Player(player1)
		self.player2 = Player(player2)
		self.score1 = 0
		self.score2 = 0
		
	def playOneGame(self):
		self.player1.rollDice()
		self.player2.rollDice()
		
		
		
	
	def playManyGames(self, numberGames):
		self.numberGames = numberGames
		while numberGames > 0:
			self.player1.rollDice()
			self.player2.rollDice()
			if self.player.getDiceValue() > self.player2.getDiceValue():
				self.player1score += 1
				numGames -=1
			elif self.player2.getDiceValue() > self.player1.getDiceValue():
				self.player2score += 1
				numGames -= 1
	
	
	def __str__(self):
		result = ''
		if self.score2 == 0 and self.score1 == 0:
			result += (f"{self.player1.name} rolled {self.player1.getDiceValue()} \n {self.player2.name} rolled {self.player2.getDiceValue()}\n")
			if self.player1.getDiceValue() > self.player2.getDiceValue():
				result += (f"{self.player1.name} has won")
			elif self.player2.getDiceValue() > self.player1.getDiceValue():
				result += (f"{self.player2.name} has won")
			else:
				result += ("It was a tie")
		else:
			result += (f"the score right now is currently {self.score1} to {self.score2}\n")
			if self.score1 > self.score2:
				result += (f"{self.player1.name} has won")
			elif self.score2 > self.score1:
				result += (f"{self.player2.name} has won")
			else:
				result += ("It was a tie")
		
		return result
'''		
d1 = Die(6)
d2 = Die(10)


player1 = Player("august", d, d2)
player1.rollDice()
print(player1)

player2 = Player("hubert", d, d2)
player2.rollDice()
print(player2)
'''

