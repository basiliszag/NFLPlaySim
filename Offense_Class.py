import pandas as pd

#Handles an NFL Offense.
#For simplicity, special teams (kickers, punters, long snappers, holders) is included in this class.
# Additionally, trick plays such as laterals/flea flickers will not be implemented.

class Offense:
	legal_plays = ["run", "pass", "field goal"]


	def __init__(self):
		""" Create an Offense consisting of a starting lineup, and two-string-deep bench. 
		Each of starters, second_string, third_string must have EXACTLY 11 players,
		while special_teams have 5 players."""
		self.starters = [] 
		self.second_string = [] 
		self.third_string = []
		self.special_teams = []
		self.play = ""
		self.fillRoster()

	def fillRoster():
		self.starters = [] 
		self.second_string = [] 
		self.third_string = []
		self.special_teams = []
		
class OffensivePlayer:
	"""Stats: 0 (terrible) to 100 (maxed out)."""
	speed = 50
	awareness = 50
	strength = 50
	agility = 50 #Basically, ability for juke moves.
	vertical = 50

	def __init__(self):
		pass
	
	def __init__(self, stats):
		speed = stats[0]
		awareness = stats[1]
		strength = stats[2]
		agility = stats[3]
		vertical = stats[4]

class QuarterBack(OffensivePlayer):
	throwPower = 50 #0 = max throw of 20 yards, 100 = maximum throw of 85 yards.
	throwAcc = 50  
	pressure_awareness = 50
	scramble_ability = 50
	tackle_break = 30

	def __init__(self, stats):
		throwPower = stats[0]
		throwAcc = stats[1]
		pressure_awareness = stats[2]
		scramble_ability = stats[3]
		tackle_break = 30	

	def throw(self, receiver):


class RunningBack(OffensivePlayer):
	acceleration = 50
	tackle_break = 50
	def __init__(self, stats):
		acceleration = stats[0]


class Receiver(OffensivePlayer):

class WideOut(Receiver):

class Slot(Receiver):

class TightEnd(Receiver):

class Lineman(OffensivePlayer):

class Center(Lineman):

class Guard(Lineman):

class Tackle(Lineman):
