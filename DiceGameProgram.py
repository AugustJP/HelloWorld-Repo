"""
August Peterson
11/16/23

This program...
"""

from DiceGameClasses import Die, Player, HighTwoGame

print("Game one:")
game1 = HighTwoGame("Matt", "Ashley")
game1.playOneGame()
print(game1)

print("")
print("Game two:")
game2 = HighTwoGame("Dexter", "Eugene")
game2.playOneGame()
print(game2)
