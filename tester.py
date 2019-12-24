#Kevin Moy presents: The NFL play simulator. 
#For simplicity, this project will not consider external 
#factors in an NFL play such as penalties and injuries. 
import Offense_Class, Defense_Class, importlib
import pandas as pd
# importlib.reload(Offense_Class)
# importlib.reload(Defense_Class)
offense = Offense_Class.Offense()
defense = Defense_Class.Defense()

offense.formation()
defense.formation()
playSim(offense, defense)

def playSim(offense, defense):
	assert offense.play != "", "Offense must run a valid play."
	assert defense.coverage != "", "Defense must have a valid formation."
	