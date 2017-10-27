import card

class explodingKitten(card):
	
	def __init__(self, location):
		self.type = "Exploding Kitten"
		self.location = location

	def __str__(self):
		card_type_Str = "An exploding kitten card"
		location = self.location
		
		
		
	def explode(self):
		# causes the player to explode if they don't have a defuse card to play, will upon drawing the card
		explosive = True
		for card in player.hand:
			if card.type == "Defuse":
				if player.deathPrompt():
					break
				else:
					explosive = False
					card.prevent_death(self)
					break
		
		if explosive:
			player.lose()

