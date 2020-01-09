import pandas as pd
import random as rd

#Handles an NFL Offense.
#For simplicity, special teams (kickers, punters, long snappers, holders) is included in this class.
# Additionally, trick plays such as laterals/flea flickers will not be implemented.

class Offense:
	legal_plays = ["run", "pass", "field goal"]
	legal_formations = ["I", "T", ]
	def __init__(self):
		""" Create an Offense consisting of a starting lineup, and two-string-deep bench. 
		Each of starters, second_string, third_string must have EXACTLY 11 players,
		while special_teams have 5 players."""
		self.starters = [] 
		self.second_string = [] 
		self.third_string = []
		self.special_teams = []
		self.formation = "I"
		self.play = "Hail Mary"
		self.fillRoster()

	def fillRoster():
		self.starters = [] 
		self.second_string = [] 
		self.third_string = []
		self.special_teams = []
		
class OffensivePlayer:
	"""Stats: 0 (terrible) to 100 (maxed out)."""
	def __init__(self, indicator):
		if indicator == 0:
			self.speed = 50
			self.awareness = 50
			strength = 50
			agility = 50 #Basically, ability for juke moves.
			vertical = 50
		elif indicator == 1:
			speed = 70
			awareness = 70
			strength = 70
			agility = 70 
			vertical = 70
		else: #Elite player. 
			speed = 90
			awareness = 90
			strength = 90
			agility = 90 
			vertical = 90

	def __init__(self, stats):
		speed = stats[0]
		awareness = stats[1]
		strength = stats[2]
		agility = stats[3]
		vertical = stats[4]

class QuarterBack(OffensivePlayer):
	throwPower = 50 #0 = max throw of 20 yards, 100 = maximum throw of 85 yards.
	maxThrowDist = 50 #50 yard pass at maximum for a 50-powered qb. 
	throwAcc = 50  
	pressure_awareness = 50
	scramble_ability = 50
	tackle_break = 30

	def __init__(self, stats):
		throwPower = stats[0]
		throwAcc = stats[1]
		pressure_awareness = stats[2]
		scramble_ability = stats[3]
		tackle_break = stats[4]	
		completed_pass = False

	def throw(self, receiver):
		if receiver.is_open and receiver.dist <= throwPower:
			completed_pass = True
		elif receiver.coverage <= (self.throwAcc + self.throwAcc) / 2:
			completed_pass = True
		else:
			completed_pass = False #Replace with some formula involving coverage level, receiver hands, qb accuracy.

class RunningBack(OffensivePlayer):
	acceleration = 50
	tackle_break = 50
	def __init__(self, stats):
		acceleration = stats[0]
		tackle_break = stats[1]


class Receiver(OffensivePlayer):
	acceleration = 50
	tackle_break = 50
	route_running = 50
	is_open = True
	dist = 0
	def __init__(self, stats):
		acceleration = stats[0]
		tackle_break = stats[1]
		route_running = stats[2]

class WideOut(Receiver):
	blocking = 50
class Slot(Receiver):
	blocking = 50
class TightEnd(Receiver):
	pass_block = 50
	run_block = 50

class Lineman(OffensivePlayer):
	pass_block = 50
	run_block = 50

class Center(Lineman):
	play_recognition = 50
class Guard(Lineman):
	pull = 50
class Tackle(Lineman):
