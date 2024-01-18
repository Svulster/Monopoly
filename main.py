from classes import Player, Street
from data import streetData
import random

board = []
players = []

def oneDice():
	return random.randint(1,6)

def twoDice():
	return random.randint(1,6) + random.randint(1,6)
	
def setup():
	for i in range(len(streetData)):
		board.append(Street(streetData[i][0], i, streetData[i][1], streetData[i][2] ,streetData[i][3], streetData[i][4]))
	availablePlayers = ["Shoe", "Ship","Car", "Hat"]
	i = 0
	noPlayers = int(input("Choose number of players: "))
	while i < noPlayers:
		print(availablePlayers)
		player = input(f"Choose player {i+1}: ")
		if player in availablePlayers:
			players.append(Player(player))
			availablePlayers.remove(player)
			i = i+1
		else:
			print("Choose a valid player")
						
if __name__ ==	"__main__":
	setup()