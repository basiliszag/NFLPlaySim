import pandas as pd
import random as rd

#Handles an NFL Offense.
#For simplicity, special teams (kickers, punters, long snappers, holders) is included in this class.
# Additionally, trick plays such as laterals/flea flickers will not be implemented.

class Offense:
	legal_plays = ["run", "pass", "field goal"]
	legal_formations = ["I", "T"]
	name = "49ers"
	play = ""

	def __init__(self, form):
		""" Create an offensive lineup, with an indicator specifying the formation/play."""
		if form == 1:
			self.QB = QuarterBack()
			self.Linemen = [Center(), Guard(), Guard(), Tackle(), Tackle()] 
			self.Receivers = [WideOut(route="Quick Slant Right"), WideOut(route="Quick Slant Left"), TightEnd()]
			self.Backs = [RunningBack(), RunningBack()]
			self.play = "Double Slants"

		elif form == 2:
			self.QB = QuarterBack()
			self.Linemen = [Center(), Guard(), Guard(), Tackle(), Tackle()] 
			self.Receivers = [WideOut(), TightEnd(), TightEnd()]
			self.Backs = [RunningBack(), RunningBack(), RunningBack()]
			self.formation = "T"
			self.play = "Sweep"

	def fillStats(self, OffensePATH):
		"""Generate team players stats from excel filepath (.xlsx),
		 which contains the starting on-field lineup and their stats."""
		stats = pd.read_excel(OffensePATH) #dataframe containing lineup

	def snap():
		""" Snap the ball/start play."""
		if play == "49ers 0:53":
			
		else:
			return 1
		
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
	qb_form = "Shotgun"

	def __init__(self, stats):
		throwPower = stats[0]
		throwAcc = stats[1]
		pressure_awareness = stats[2]
		scramble_ability = stats[3]
		tackle_break = stats[4]	
		completed_pass = False

	def __init__(self, ind):
		if ind

	def throw(self, receiver):
		if receiver.is_open and receiver.dist <= throwPower:
			completed_pass = True
		elif receiver.coverage <= 5 and receiver.safety_presence <= 6:
			completed_pass = True
		else:
			completed_pass = False #Replace with some formula involving coverage level, receiver hands, qb accuracy.

class RunningBack(OffensivePlayer):
	acceleration = 50
	tackle_break = 50
	def __init__(self, stats):
		self.acceleration = stats[0]
		self.tackle_break = stats[1]


class Receiver(OffensivePlayer):
	acceleration = 50
	tackle_break = 50
	route_running = 50
	is_open = True
	dist = 0
	route = ""
	coverage = 5
	safety_presence = 5
	def __init__(self, stats):
		self.acceleration = stats[0]
		self.tackle_break = stats[1]
		self.route_running = stats[2]
	def __init__(self, route):
		self.route = route

class WideOut(Receiver):
	blocking = 50
	role = "route"
	def __init__(self, route):
		self.route = route		
class Slot(Receiver):
	blocking = 50
	role = "route"
	def __init__(self, route):
		self.route = route	
class TightEnd(Receiver):
	pass_block = 50
	run_block = 50
	role = "route"
class Lineman(OffensivePlayer):
	pass_block = 50
	run_block = 50
class Center(Lineman):
	play_recognition = 50
class Guard(Lineman):
	pull = 50
class Tackle(Lineman):
	pass