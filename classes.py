class Player():
	def __init__(self, name):
			self.name = name
			self.money = 30000
			self.position = 0
			self.property = []
			self.jail = False
			self.jailCounter = 0
		
	def move(self, change):
		for i in range(change):
			if self.position < 39:
				self.position += 1
				#print(self.position)
			else:
				self.position = 0
				#print(self.position)
			if self.position == 0:
				self.money = self.money + 4000

class BoardTile():
	def __init__(self, name, position, tileType) -> None:
		self.position = position
		self.type = tileType
		self.name = name

class StreetTile(BoardTile):
	def __init__(self, name, position, price, housePrice, rent, mortgageValue, set, tileType="StreetTile") -> None:
		super().__init__(name, position, tileType)
		self.tileType = tileType
		self.price = price
		self.housePrice = housePrice
		self.houseLevel = 0
		self.rent = rent
		self.position = position
		self.mortgageValue = mortgageValue
		self.mortgaged = False
		self.owner = "City"
		self.set = set
		
	def getRent(self):
		return self.rent[self.houseLevel]
		
	def updateHouseLevel(self, change):
		self.houseLevel = self.houseLevel + change

class CardTile(BoardTile):
	def __init__(self, name, position, tileType = "CardTile") -> None:
		super().__init__(name, position, tileType)
		self.tileType = tileType

	def getCard():
		pass

class UtilitiesTile(BoardTile):
	def __init__(self, name, position, price, mortgageValue, set, tileType="UtilitiesTile") -> None:
		super().__init__(name, position, tileType)
		self.tileType = tileType
		self.price = price
		self.mortgageValue = mortgageValue
		self.owner = "City"
		self.set = set
	
	def getRent(self):
		pass

class TaxTile(BoardTile):
	def __init__(self, name, position, rent, tileType = "TaxTile") -> None:
		super().__init__(name, position, tileType)
		self.tileType = tileType
		self.rent = rent

class OtherTile(BoardTile):
	def __init__(self, name, position, rent, tileType = "OtherTile") -> None:
		super().__init__(name, position, tileType)
		self.tileType = tileType
		self.rent = rent