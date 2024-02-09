#			name, position, price, housePrice, rent, mortgageValue, set
streetData=[["Västerlånggatan", 1, 1200, [0] [0], [0] ["Västerlånggatan","Hornsgatan"]],
			["Hornsgatan", 3, 1200, [0] [0], [0] ["Västerlånggatan","Hornsgatan"]],
			["Södra station", 5, 4000, [0] [0], [0] ["Södra station", "Östra station", "Norra staion", "Centralstation"]],
			["Folkungagatan", 6, 2000, [0] [0], [0] ["Folkungagatan", "Götgatan", "Ringvägen"]],
			["Götgatan", 8, 2000, 1000, [100, 550, 1700, 5150, 7600, 9500], 1000, ["Folkungagatan", "Götgatan", "Ringvägen"]],
			["Ringvägen", 9, 2400, [0] [0], [0] ["Folkungagatan", "Götgatan", "Ringvägen"]],
			["S:t Eriksgatan", 11, 2800, [0] [0], [0] ["S:t Eriksgatan", "Odengatan", "Valhallavägen"]],
			["Odengatan", 13, 2800, [0] [0], [0] ["S:t Eriksgatan", "Odengatan", "Valhallavägen"]],
			["Valhallavägen", 14, 3300, [0] [0], [0] ["S:t Eriksgatan", "Odengatan", "Valhallavägen"]],
			["Östra station", 15, 4000, [0] [0], [0] ["Södra station", "Östra station", "Norra staion", "Centralstation"]],
			["Sturegatan", 16, 3600, [0] [0], [0] ["Sturegatan", "Karlavägen", "Narvavägen"]],
			["Karlavägen", 18, 3600, [0] [0], [0] ["Sturegatan", "Karlavägen", "Narvavägen"]],
			["Narvavägen", 19, 4000, [0] [0], [0] ["Sturegatan", "Karlavägen", "Narvavägen"]],
			["Strandvägen", 21, 4400, [0] [0], [0] ["Strandvägen", "Kungsträdgårdsgatan", "Hamngatan"]],
			["Kungsträdgårdsgatan", 23, 4400, [0] [0], [0] ["Strandvägen", "Kungsträdgårdsgatan", "Hamngatan"]],
			["Hamngatan", 24, 4800, [0] [0], [0] ["Strandvägen", "Kungsträdgårdsgatan", "Hamngatan"]],
			["Centralstation", 25, 4000, [0] [0], [0] ["Södra station", "Östra station", "Norra staion", "Centralstation"]],
			["Vasagatan", 26, 5200, [0] [0], [0] ["Vasagatan", "Kungsgatan", "Stureplan"]],
			["Kungsgatan", 27, 5200, [0] [0], [0] ["Vasagatan", "Kungsgatan", "Stureplan"]],
			["Stureplan", 29, 5600, [0] [0], [0] ["Vasagatan", "Kungsgatan", "Stureplan"]],
			["Gustav Adolfs torg", 31, 6000, [0] [0], [0] ["Gustav Adolfs torg", "Drottninggatan", "Diplomatstaden"]],
			["Drottninggatan", 32, 6000, [0] [0], [0] ["Gustav Adolfs torg", "Drottninggatan", "Diplomatstaden"]],
			["Diplomatstaden", 34, 6400, [0] [0], [0] ["Gustav Adolfs torg", "Drottninggatan", "Diplomatstaden"]],
			["Norra station", 35, 4000, [0] [0], [0] ["Södra station", "Östra station", "Norra staion", "Centralstation"]],
			["Centrum", 37, 7000, [0] [0], [0] ["Centrum", "Norrmalmstorg"]],
			["Norrmalmstorg", 39, 8000, [0] [0], [0] ["Centrum", "Norrmalmstorg"]]]

#				name, position, 
cardTileData = [["Allmänning", 2],
				["Chans", 7],
				["Allmänning", 17],
				["Chans", 22],
				["Allmänning", 33],
				["Chans", 36]]

#			name, position, price, mortgageValue, owner, set
utilitiesData= [["Elverket", 12, 3000, [0] ["Elverket", "Vattenreningsverket"]],
            	["Vattenreninsverket", 28, 3000, [0] ["Elverket", "Vattenreningsverket"]]]

taxTileData=[["Inkomstskatt", 4, 4000],
			["Lyxskatt", 38, 2000]]

#			name, position, rent
otherTileData=[["Gå", 0, [-4000]],	
			["Fängelse", 10, [0]],
            ["Fri parkering", 20, [0]],
			["Gå i fängelse", 30, [0]],
]