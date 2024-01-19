class Player():
	def __init__(self, name):
			self.name = name
			self.money = 30000
			self.position = 0
			self.property = []
			self.jail = False
		
	def move(self, change):
		for i in range(change):
			if self.position < 39:
				self.position += 1
				print(self.position)
			else:
				self.position = 0
				print(self.position)
			if self.position == 0:
				self.money = self.money + 4000
		
class Street():
	def __init__(self, name, position, price, housePrice, rent, mortgageValue, owner, set):
		self.name = name
		self.price = price
		self.housePrice = housePrice
		self.houseLevel = 0
		self.rent = rent
		self.position = position
		self.mortgageValue = mortgageValue
		self.mortgaged = False
		self.owner = owner
		self.set = set
		
	def getRent(self):
		return self.rent[self.houseLevel]
		
	def updateHouseLevel(self, change):
		self.houseLevel = self.houseLevel + change