import pandas as pd
class Defense:
	legalCoverages = ["3-4"]
	name = "Vikings"
	def __init__(self):
		self.starters = []
		self.second_string = [] 
		self.third_string = []
		self.coverage = ""

	def generateTeam(self, DefensePATH):
		"""Generate team players from excel path (.xlsx)."""
		df = pd.read_excel(OffensePATH)

class DefensivePlayer:
	"""Stats: 0 (terrible) to 100 (maxed out)."""
	speed = 50
	awareness = 50
	strength = 50
	agility = 50 
	vertical = 50
	def __init__(self):
		pass

	def __init__(self, stats):
		speed = stats[0]
		awareness = stats[1]
		strength = stats[2]
		agility = stats[3]
		vertical = stats[4]

class Lineman(DefensivePlayer):
	pass
class DTackle(Lineman):
	pass
class DEnd(Lineman):
	pass
class Linebacker(DefensivePlayer):		
	pass
class MLB(Linebacker):
	pass
class InsideLB(Linebacker):
	pass
class OutsideLB(Linebacker):
	pass
class Cornerback(DefensivePlayer):
	pass
class Safety(DefensivePlayer):
	pass