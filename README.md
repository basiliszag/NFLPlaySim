# NFLPlaySim
Simplified Simulation of an NFL play given players, statistics, and a playbook. 

This program attempts to simulate an NFL play through object-oriented programming. 
An NFL play consists of an offense and defense, both of which contain 11 players. 
Each the offense and defense MUST consist of eleven players at a time, with twenty-two players making up the second and third depth bench.
For simplicity, only fundamental passing, running, and special teams plays will be considered (no trick plays).

Attribute statistics for players are graded on a range from 0 to 100, where 0 = complete incompetence and 100 = mastery. 
For example, Lamar Jackson will receive a near 100 rating for elusiveness. 

In-play statistics such as QB pressure or coverage on a receiver will be given on a scale from 0 to 10. 
Meaning of the ranking, is, of course, dependent on the statistic. 
For example, a 0 ranking for coverage on a receiver means he is wide open, and 10 means he is not open at all. 

There exist many factors into developing how an NFL play is completed.

1. PASS ATTEMPTS. 
A completion of a pass from a quarterback to a wide receiver is dependent on four in-play factors:
	- QB pressure
	- Distance to receiver
	- Coverage on receiver
	- Safety presence
2. RUN ATTEMPTS
A handoff to a runningback/fullback's net running distance is calculated by these factors:
	- Runningback fullback acceleration,speed,toughness,and elusiveness. (Positive)
	- Defensive scheme (If a defensive formation is known to limit run yards, such as a 5-2 defense, then the net run yards will be affected negatively.)
	- Offensive Linemen blocking ability 
3. SPECIAL TEAMS PLAYS 
Special teams plays are greatly simplified in this simulator.
	-The chance that a field goal is missed is solely determined by the distance to the goalposts (= distance to endzone + 17 yards).
	-The chance that a kickoff is returned for a touchdown is always 3 percent. Otherwise, kickoffs automatically become touchbacks (opponent's ball at their 25 yard line)
	-Punters are assumed as total perfect machines here, due to the completely unpredictable nature of a punted football. A punter will always kick for 50 yards. If the punting team is beyond their opponent's 50 yard line, the punter will kick the ball to the opponent's 5 yard line. 
