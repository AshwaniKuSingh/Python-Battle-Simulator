# Python-Battle-Simulator

A simple battle simulator that pits one army against another.

# The Basic Game

At the start of the game, each commander is given a starting total of $10. Units are purchased and stored in their army. The commanders may spend as much or as little of their money as they desire. After the armies are assembled, the units are then made to fight each other in the order they were purchased in. Each unit in the standard game costs $1.

There are three types of units available:

• Archer  
• Soldier  
• Knight  

Each unit has a weakness and a strength. Archers are good against Soldiers but are terrible against Knights. Soldiers are good against Knights but can’t win against Archers. Knights beat Archers, but fall short against Soldiers. If a unit comes up against a unit of the same type, both lose. Table 1 indicates who wins in any encounter.
 Type of Unit Archer Soldier Knight
 
 |  Type of Unit | Archer  | Soldier  | Knight  |
 |  -----------  | ------  | -------  | -----   |
 | Archer        | Tie     |  Archer  | Knight  |
 | Soldier       | Archer  |  Tie     | Soldier |
 | Knight        | Knight  |  Soldier | Tie     |  
 
  Table 1: Outcomes of battles when units enter combat.  
  
After each fight, the winner is left on the battlefield to fight the next combatant. If both units lose, then two new units are taken from the army and begin their fight.

# The Extended Game

Extended game is upgradation of **Basic Game**. The two upgrades to the basic game is as following:  

1. Improved Combat<br>
Combat is very simple in the original game, you can try to implement an improved version of the combat by using the following rules:<br>
• In the cases where a unit would win, it instead deals its damage before the other unit is able to deal theirs. Soldiers hit Knights first, Archers hit Soldiers first, and Knights hit Archers first.<br>
• Knights are able to trample other units. If the Knight is fighting an Archer and the unit behind the Archer is another Archer, then the Knight deals its damage to both Archers.<br>
• If an Archer is at the front of its army but not in battle, they deal their damage to the opposing unit if they are still alive at the end of combat.<br>
The changes made here effectively change the order of combat which may impact further based on choices below.
on.
2. Medics<br>
Money remaining after the purchasing of armies will be used to hire and outfit medics. When a unit dies, it will be returned to the pool at the back of the army. Each time this happens, supplies for the medics decreases. Once the medics have no supplies left, they will be unable to save any more units.<br>
Medics are hired and supplied at $1 per unit. All money at the end of army creation is spent on Medics.<br>


