from classes import *
from data import *
import random
import os

board = [None] * 40
players = []
noHouses = 32
noHotels = 12

def oneDice():
	return random.randint(1,6)

def twoDice():
	return random.randint(1,6) + random.randint(1,6)
	
def setup():
	os.system("cls")

	#add street data to the board
	for i in range(len(streetData)):
		board[streetData[i][1]] = StreetTile(streetData[i][0], streetData[i][1], streetData[i][2] ,streetData[i][3], streetData[i][4], streetData[i][5], streetData[i][6])
	for i in range(len(cardTileData)):
		board[cardTileData[i][1]] = CardTile(cardTileData[i][0], cardTileData[i][1])
	for i in range(len(utilitiesData)):
		board[utilitiesData[i][1]] = UtilitiesTile(utilitiesData[i][0], utilitiesData[i][1], utilitiesData[i][2] ,utilitiesData[i][3], utilitiesData[i][4])
	for i in range(len(taxTileData)):
		board[taxTileData[i][1]] = TaxTile(taxTileData[i][0], taxTileData[i][1], taxTileData[i][2])
	for i in range(len(otherTileData)):
		board[otherTileData[i][1]] = OtherTile(otherTileData[i][0], otherTileData[i][1], otherTileData[i][2])

	availablePlayers = ["Battleship", "Wheelbarrow", "Thimble", "Boot", "Car", "Hat", "Cat", "Dog"]
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

def buyStreet(buyer, street):
	reply = input(f"Currently owned by {street.owner}. Would you like to buy for ${street.price}? (y/n) ")
	if reply == "y":
		if buyer.money < street.price:
			print("You don't have enough money")
		else:
			buyer.money -= street.price
			street.owner = buyer.name
			buyer.property.append(street)
			print(f"{buyer.name} bought {street.name}!")

def payRent(player, street):
	print(f"{board[player.position].name} is owned by {street.owner}!")
	rent = street.getRent()
	print(f"Pay ${rent} in rent to {street.owner}!")
	player.money -= rent
	for player in players:
		if player.name == street.owner:
			player.money += rent

def mortgage(player, streetName):
	while True:
		print("Your properties:")
		properties = []
		for street in player.property:
			print(street.name)
			properties.append(street.name)
		streetName = input(f"Choose street to mortgage:")
		if streetName in properties:
			for street in board:
				if street.name == streetName and street.mortgaged == False:
					player.money += street.mortgageValue
					street.mortgaged == True
			cont = input("Choose another street to mortgage? (y/n)")
			if cont == "n":
				break
		elif streetName == "exit":
			break
		else:
			print("Choose a valid street name")
	


def round(currentPlayer):
	os.system("cls")
	print(f"Current player: {currentPlayer.name}")
	print(f"Your current amount of money is: {currentPlayer.money}")

	if currentPlayer.property != []: 
		mortgageProperty = input("Do you want to (un)mortgage property/properties? (y/n): ")
		if mortgageProperty == "y":
			mortgage()

		#Add check if player owns a complete set of streets, and a choice to buy buildings

	input("Throw dice? ")
	while True:
		throw = [oneDice(), oneDice()]
		print(f"Dice throw result: {throw[0]} + {throw[1]}")
		
		diceCounter = 0
		if throw[0] == throw[1]:
			diceCounter += 1
			if diceCounter == 3:
				currentPlayer.position = 10
				currentPlayer.jail = True
				print(f"{currentPlayer.name} threw a pair three times in a row and went to {board[currentPlayer.position].name}!")
		
		currentPlayer.move(throw[0]+throw[1])
		print(f"Current position: {board[currentPlayer.position].name}")

		if board[currentPlayer.position].tileType == "StreetTile":
			if board[currentPlayer.position].owner == "City":
				buyStreet(currentPlayer, board[currentPlayer.position])
			elif board[currentPlayer.position].owner != "City" and board[currentPlayer.position].owner != currentPlayer.name:
				payRent(currentPlayer, board[currentPlayer.position])
			elif board[currentPlayer.position].owner == currentPlayer.name:
				print("Visiting your own property!")

		if board[currentPlayer.position].tileType == "TaxTile":
			print(f"Pay {board[currentPlayer.position].rent} in taxes!")
			currentPlayer.money -= board[currentPlayer.position].rent

		if throw[0] != throw[1]:
			break

	input("End Turn")


#	if diceThrow:
#		throw = twoDice()
#		print(f"Dice throw result: {throw}")
#		currentPlayer.move(throw)
#		print(f"Current position: {board[currentPlayer.position].name}")
#		if board[currentPlayer.position].owner == "City":
#			buy = input(f"Currently owned by the bank. Would you like to buy for ${board[currentPlayer.position].price}? (y/n) ")
#			if buy == "y":
#				if currentPlayer.money < board[currentPlayer.position].price:
#					print("You don't have enough money")
#				else:
#					currentPlayer.money -= board[currentPlayer.position].price
#					board[currentPlayer.position].owner = currentPlayer.name
#					print(f"{currentPlayer.name} bought {board[currentPlayer.position].name}!")
#		elif board[currentPlayer.position].owner == currentPlayer.name:
#			print("Visiting your own property")
#		elif board[currentPlayer.position].owner == "Bank":
#			pass # Add function to check for "Go to jail" etc.
#		else:
#			print(f"{board[currentPlayer.position].name} is owned by {board[currentPlayer.position].owner}!")
#			rent = board[currentPlayer.position].getRent()
#			print(f"Pay ${rent} in rent!")
#			currentPlayer.money -= rent
#			for player in players:
#				if player.name == board[currentPlayer.position].owner:
#					player.money += rent 

if __name__ ==	"__main__":
	setup()
	game()
