class Player():
	def __init__(self, name):
			self.name = name
			self.money = 4000
			self.position = 0
			self.property = []
		
	def move(self, change):
		for i in range(change):
			if self.position < 40:
				self.position += 1
			else:
				self.position = 0
			if self.position == 0:
				self.money = self.money + 4000
		
class Street():
	def __init__(self, name, position, price, housePrice, rent, mortgageValue):
		self.name = name
		self.price = price
		self.housePrice = housePrice
		self.houseLevel = 0
		self.rent = rent
		self.position = position
		self.mortgageValue = mortgageValue
		self.mortgaged = False
		self.owner = "Bank"
		
	def getRent(self):
		return self.rent[self.houseLevel]
		
	def updateHouseLevel(self, change):
		self.houseLevel = self.houseLevel + change

#test script
if __name__ == "__main__":
	testplayer = Player("Shoe")
	testplayer.move(43)
	print(f"Player position: {testplayer.position}")
	print(testplayer.money)

	print("")

	testStreet = Street("Norrmalmstorg", 39, 8000, 120, [200, 400, 800, 1200, 1600, 2000], None)
	print(testStreet.getRent())
	testStreet.updateHouseLevel(4)
	print(testStreet.getRent())
	testStreet.updateHouseLevel(-2)
	print(testStreet.getRent())