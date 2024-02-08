from classes import Player, StreetTile, CardTile
from data import streetData, cardTileData
import random
import os

board = [None] * 40
players = []

def oneDice():
	return random.randint(1,6)

def twoDice():
	return random.randint(1,6) + random.randint(1,6)
	
def setup():
	for i in range(len(streetData)):
		board[streetData[i][1]] = StreetTile(streetData[i][0], streetData[i][1], streetData[i][2] ,streetData[i][3], streetData[i][4], streetData[i][5], streetData[i][6], streetData[i][7])
	for i in range(len(cardTileData)):
		board[cardTileData[i][1]] = (CardTile(cardTileData[i][0], cardTileData[i][1]))
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

def game():
	i = 0
	while i < len(players):
		print("")
		if len(players) == 1:
			print(f"{players[i].name} has won the game!")
			print(f"Total bank balance: {players[i].money}")
			print(f"Total amount of streets owned: {len(players[i].property)}")
			break

		round(players[i])

		if players[i].money <= 0 and players[i].property == None:
			print(f"{players[i].name} has gone bankrupt!")
			players.remove(i)

		i += 1

		if i == len(players):
			i = 0

def round(currentPlayer):
	#os.system("cls")
	print(f"Current player: {currentPlayer.name}")
	print(f"Your current amount of money is: {currentPlayer.money}")
	if currentPlayer.property != None:
		pass #Add choice to buy houses or hotels.
	diceThrow = input("Throw dice? ")
	if diceThrow:
		throw = twoDice()
		print(f"Dice throw result: {throw}")
		currentPlayer.move(throw)
		print(f"Current position: {board[currentPlayer.position].name}")
		if board[currentPlayer.position].owner == "City":
			buy = input(f"Currently owned by the bank. Would you like to buy for ${board[currentPlayer.position].price}? (y/n) ")
			if buy == "y":
				if currentPlayer.money < board[currentPlayer.position].price:
					print("You don't have enough money")
				else:
					currentPlayer.money -= board[currentPlayer.position].price
					board[currentPlayer.position].owner = currentPlayer.name
					print(f"{currentPlayer.name} bought {board[currentPlayer.position].name}!")
		elif board[currentPlayer.position].owner == currentPlayer.name:
			print("Visiting your own property")
		elif board[currentPlayer.position].owner == "Bank":
			pass # Add function to check for "Go to jail" etc.
		else:
			print(f"{board[currentPlayer.position].name} is owned by {board[currentPlayer.position].owner}!")
			rent = board[currentPlayer.position].getRent()
			print(f"Pay ${rent} in rent!")
			currentPlayer.money -= rent
			for player in players:
				if player.name == board[currentPlayer.position].owner:
					player.money += rent

if __name__ ==	"__main__":
	setup()
	game()
