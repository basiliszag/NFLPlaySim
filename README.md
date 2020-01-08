# NFLPlaySim
Simplified Simulation of an NFL play given players, statistics, and a playbook. 

The program attempts to simulate an NFL play through object-oriented programming. 
An NFL play consists of an offense and defense, both of which contain 11 players. 
Each the offense and defense MUST consist of eleven players at a time, with twenty-two players making up the second and third depth bench.
For simplicity, only fundamental passing, running, and special teams plays will be considered (no trick plays).

Attribute statistics for players are graded on a range from 0 to 100, where 0 = complete incompetence and 100 = mastery. 
For example, Lamar Jackson will receive a near 100 rating for elusiveness. 

In-play statistics such as QB pressure or coverage on a receiver will be given on a scale from 0 to 10. 
Meaning of the ranking, is, of course, dependent on the statistic. 
For example, a 0 ranking for coverage on a receiver means he is wide open, and 10 means he is not open at all. 

There exist many factors into developing how an NFL play is completed.

1. PASS ATTEMPTS. A quarterback may attempt a pass IF his VISION > 50 AND 
